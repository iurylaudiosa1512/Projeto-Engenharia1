ETL COVID Brasil - Projeto de Monitoramento

Projeto para coletar, armazenar e visualizar dados de COVID-19 no Brasil utilizando Docker, Airflow, PostgreSQL e Grafana.

Tecnologias

Docker

Airflow

PostgreSQL

Grafana

Python

Estrutura

dags/ → DAGs do Airflow

sql/ → Scripts de inicialização do PostgreSQL

docker-compose.yml → Configuração dos containers

Como Rodar

Subir os containers:

docker-compose up -d


Acessar o Airflow: http://localhost:8080

Usuário: admin

Senha: admin

Acessar o Grafana: http://localhost:3000

Usuário: admin

Senha: admin

Criar dashboards no Grafana conectando ao PostgreSQL e consultar a evolução dos casos.

Objetivo

Visualizar a evolução diária de casos de COVID-19 por estado no Brasil.


<img width="1607" height="641" alt="image" src="https://github.com/user-attachments/assets/3b4ca9fd-6cc4-4f0f-82ff-0360e0b04d67" />
