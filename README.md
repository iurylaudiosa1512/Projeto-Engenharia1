# ETL COVID Brasil - Airflow + Docker + Grafana

Este projeto realiza a coleta, armazenamento e visualização de dados de COVID-19 no Brasil utilizando **Airflow**, **PostgreSQL**, **Docker** e **Grafana**.  

Os dados são extraídos da API pública: [COVID-19 Brazil API](https://covid19-brazil-api.vercel.app/).

---

## Funcionalidades

- **Extração (Extract):** Busca os dados atualizados da API.
- **Transformação/Preparação (Transform/Load):** Armazena os dados no PostgreSQL.
- **Carga (Load):** Cria tabela `covid_data` e popula com informações sobre casos e mortes.
- **Visualização:** Permite criar gráficos de evolução de casos recentes no Grafana.

---

## Tecnologias utilizadas

- [Docker](https://www.docker.com/) – Para containerização do projeto.
- [Docker Compose](https://docs.docker.com/compose/) – Para orquestração dos containers.
- [Apache Airflow](https://airflow.apache.org/) – Para orquestração do pipeline ETL.
- [PostgreSQL](https://www.postgresql.org/) – Banco de dados relacional.
- [Grafana](https://grafana.com/) – Para dashboards e visualização de dados.
- [Python](https://www.python.org/) – Para scripts de ETL.
- [Requests](https://pypi.org/project/requests/) – Para acessar a API.

---


<img width="1607" height="641" alt="image" src="https://github.com/user-attachments/assets/3b4ca9fd-6cc4-4f0f-82ff-0360e0b04d67" />
