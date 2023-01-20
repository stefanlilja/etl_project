from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime
from random import randint

import sys 
import os
import glob
sys.path.append('/mnt/c/Users/Stefan/Documents/Modul9/etl_project/')
paths = glob.glob('/mnt/c/Users/Stefan/Documents/Modul9/etl_project/*')

for path in paths:
    if os.path.isdir(path):
        sys.path.append(path)

import weather
#from weather import testing

#weather.download_from_api()
#weather.testing()



with DAG(
    dag_id="forecast_dag",
    start_date=datetime(2023,1,1),
    schedule_interval="0 0 * * *",
    catchup=False
) as dag:
    download_data = PythonOperator(
        task_id = "download_data",
        python_callable=weather.download_from_api
    )
    

    [download_data]