from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys

sys.path.append('/opt/airflow/scripts')

from get_weather import get_weather
from get_energy import get_energy 
from merge_energy_weather import merge_energy_weather

default_args = {
    'start_date': datetime(2024, 1, 1),
    'catchup': False,
}

with DAG('energy_weather_pipeline', default_args=default_args, schedule_interval='@daily', catchup=False) as dag:

    task_weather = PythonOperator(
        task_id='get_weather',
        python_callable=get_weather,
    )

    task_conso = PythonOperator(
        task_id='get_consumption',
        python_callable=get_energy,
    )

    task_merge = PythonOperator(
        task_id='merge_data',
        python_callable=merge_energy_weather,
    )

    # Ordre d'exécution
    task_weather >> task_conso >> task_merge
