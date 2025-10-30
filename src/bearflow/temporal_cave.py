# ⏳ Temporal
from datetime import timedelta
from temporalio import activity, workflow
from temporalio.client import Client
from temporalio.worker import Worker


@activity.defn
async def task_a():
    print("Temporal: Task A complete")


@activity.defn
async def task_b():
    print("Temporal: Task B complete")


@workflow.defn
class MyFlow:
    @workflow.run
    async def run(self):
        await workflow.execute_activity(task_a, schedule_to_close_timeout=timedelta(seconds=10))
        await workflow.execute_activity(task_b, schedule_to_close_timeout=timedelta(seconds=10))
        print("Temporal flow complete!")


async def main():
    client = await Client.connect("localhost:7233")
    worker = Worker(
        client, task_queue="myflow", workflows=[MyFlow], activities=[task_a, task_b]
    )
    await worker.run()


# Requires a running Temporal server (`temporal server start-dev`)
