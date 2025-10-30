# ⚙️  Celery
from celery import Celery

app = Celery("myflow", broker="redis://localhost:6379/0")


@app.task
def task_a():
    print("Celery: Task A complete")


@app.task
def task_b():
    print("Celery: Task B complete")


# To run this POC:
#   celery -A celery_den worker --loglevel=info
# Then, in another shell:
#   from celery_den import task_a, task_b
#   task_a.delay(); task_b.delay()
