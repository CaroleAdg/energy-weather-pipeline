from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys

sys.path.append('/opt/airflow/scripts')

from train_model import train_and_save_model

default_args = {
    'start_date': datetime(2024, 1, 1),
    'catchup': False,
}

with DAG('train_model_dag', default_args=default_args, schedule_interval='@daily', catchup=False) as dag:

    task_train = PythonOperator(
        task_id='train_model',
        python_callable=train_and_save_model,
    )

    # Ordre d'exécution
    task_train
