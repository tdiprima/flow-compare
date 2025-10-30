"""
Airflow DAG with two sequential Python tasks.

Creates aircub_dag with task_a >> task_b dependency chain, manual trigger only.
Place in Airflow dags/ folder and trigger via Airflow UI or: airflow dags trigger aircub_dag
"""
# 🪶 Airflow-lite (aka basic Airflow DAG)
from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator


def task_a():
    print("Airflow-lite: Task A complete")


def task_b():
    print("Airflow-lite: Task B complete")


with DAG(
    "aircub_dag",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:
    a = PythonOperator(task_id="task_a", python_callable=task_a)
    b = PythonOperator(task_id="task_b", python_callable=task_b)
    a >> b
