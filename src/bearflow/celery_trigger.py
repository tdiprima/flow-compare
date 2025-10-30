from celery_den import task_a, task_b

task_a.delay()
task_b.delay()
