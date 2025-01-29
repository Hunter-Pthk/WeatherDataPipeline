import sys
import os
from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pipelines.weather_pipeline import weather_pipeline

default_args = {
    'owner' : 'Nikesh Pathak',
    'start_date' : datetime(2025, 1, 28)
}
file_postfix = datetime.now().strftime("%Y%m%d")

dag = DAG(
    dag_id='etl_weather_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    tags=['weather','etl','pipeline']
)

# Extraction from Weather api
extract = PythonOperator(
    task_id='Weather_extraction',
    python_callable=weather_pipeline,
    op_kwargs={'file_name1': f'weather_current_{file_postfix}',
               'file_name2': f'weather_forecast_{file_postfix}'
               },
    dag = dag
)