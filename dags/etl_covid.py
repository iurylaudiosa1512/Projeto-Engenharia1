from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import requests
import psycopg2

API_URL = "https://covid19-brazil-api.vercel.app/api/report/v1"

DB_CONFIG = {
    "dbname": "covid",
    "user": "airflow",
    "password": "airflow",
    "host": "postgres",
    "port": "5432"
}

def create_table():
    """Cria a tabela covid_data caso não exista"""
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS covid_data (
            id SERIAL PRIMARY KEY,
            date TIMESTAMP,
            location VARCHAR(100),
            total_cases BIGINT,
            new_cases BIGINT,
            total_deaths BIGINT,
            new_deaths BIGINT,
            UNIQUE(date, location)
        );
    """)
    conn.commit()
    cur.close()
    conn.close()
    print("[SETUP] Tabela covid_data criada ou já existente.")

def extract_data():
    """Extrai dados da API e salva temporariamente"""
    response = requests.get(API_URL)
    if response.status_code != 200:
        raise Exception(f"Erro ao acessar API: {response.status_code}")
    data = response.json()
    records = data.get("data", [])
    print(f"[EXTRACT] {len(records)} registros extraídos")
    import json
    with open("/tmp/covid_data.json", "w", encoding="utf-8") as f:
        json.dump(records, f)

def load_data():
    """Carrega os dados no PostgreSQL"""
    import json
    with open("/tmp/covid_data.json", "r", encoding="utf-8") as f:
        records = json.load(f)

    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    for rec in records:
        cur.execute("""
            INSERT INTO covid_data (date, location, total_cases, new_cases, total_deaths, new_deaths)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON CONFLICT (date, location) DO NOTHING;
        """, (
            rec.get("datetime"),           # data
            rec.get("state"),              # estado
            rec.get("cases"),              # total_cases
            rec.get("confirmed") - rec.get("cases") if rec.get("confirmed") and rec.get("cases") else 0,  # new_cases
            rec.get("deaths"),             # total_deaths
            rec.get("deaths")              # new_deaths (ajustável)
        ))
    conn.commit()
    cur.close()
    conn.close()
    print(f"[LOAD] {len(records)} registros carregados no banco")

with DAG(
    "etl_covid_brazil_api_full",
    start_date=datetime(2023, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    tags=["covid"]
) as dag:

    t0 = PythonOperator(task_id="create_table", python_callable=create_table)
    t1 = PythonOperator(task_id="extract", python_callable=extract_data)
    t2 = PythonOperator(task_id="load", python_callable=load_data)

    t0 >> t1 >> t2
