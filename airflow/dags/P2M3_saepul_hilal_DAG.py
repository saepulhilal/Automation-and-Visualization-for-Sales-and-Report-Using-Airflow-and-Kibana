# '''
# ================================================================================================================================================================

# Nama : Saepul Hilal

# Batch : HCK - 010

# File ini bertujuan untuk membuat task. Task yang akan dibuat adalah untuk fetching dataset, cleaning dataset dan push ke elasticserch

# ================================================================================================================================================================
# '''

# import datetime as dt
# from datetime import timedelta
# from airflow import DAG 
# from airflow.operators.python import PythonOperator

# from steps.fetch import fetching_data # Import fungsi fetching_data dari file fetch.py
# from steps.clean import cleaning_data # Import fungsi cleaning_data dari file clean.py
# from steps.push import push_to_elastic # Import fungsi push_to_elastic dari file push.py


# from airflow.models import DAG

# from airflow.operators.python import PythonOperator
# from airflow.providers.postgres.operators.postgres import PostgresOperator
# from airflow.utils.task_group import TaskGroup
# from datetime import datetime
# from sqlalchemy import create_engine, insert
# import pandas as pd



# default_args = {
#     'owner': 'sapul',
#     'start_date': datetime(2023, 12, 25),
#     'retries': 1,
#     'retry_delay': timedelta(minutes=5),
# }

# with DAG(
#     'fetching_cleaning_push_elastic',
#     default_args=default_args,
#     schedule_interval='30 06 * * *', # mengatur pengulangan setiap 06.30
#     ) as dag:
    
#     fetching = PythonOperator(
#         task_id='Fetch_from_Postgresql',
#         python_callable=fetching_data
#     )

#     cleaning = PythonOperator(
#         task_id='Data_Cleaning',
#         python_callable=cleaning_data
#     )

#     push_elastic = PythonOperator(
#         task_id='Post_to_Elasticsearch',
#         python_callable=push_to_elastic
#     )

#     # langkah pelaksanaan
#     fetching >> cleaning >> push_elastic