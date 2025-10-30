"""
Prefect workflow implementation with two sequential tasks.

Executes task_a and task_b using Prefect's @task and @flow decorators.
Run directly with: python myflow_prefect.py
"""
# 🌀 Prefect
from prefect import flow, task


@task
def task_a():
    print("Prefect: Task A complete")


@task
def task_b():
    print("Prefect: Task B complete")


@flow
def myflow():
    task_a()
    task_b()
    print("Prefect flow complete!")


if __name__ == "__main__":
    myflow()
