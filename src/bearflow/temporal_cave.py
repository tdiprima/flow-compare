"""
Temporal durable workflow implementation with async activities.

Defines MyFlow workflow that executes task_a and task_b as activities with 10s timeouts.
Requires running Temporal server: temporal server start-dev
Start worker: python temporal_cave.py
"""
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
        await workflow.execute_activity(
            task_a, schedule_to_close_timeout=timedelta(seconds=10)
        )
        await workflow.execute_activity(
            task_b, schedule_to_close_timeout=timedelta(seconds=10)
        )
        print("Temporal flow complete!")
        # No return statement = returns None
        return "Workflow executed successfully!"


async def main():
    client = await Client.connect("localhost:7233")
    worker = Worker(
        client, task_queue="myflow", workflows=[MyFlow], activities=[task_a, task_b]
    )

    # Run worker with proper signal handling
    print("Worker started. Press Ctrl-C to shutdown gracefully.")
    try:
        await worker.run()
    except KeyboardInterrupt:
        print("\nShutdown signal received, stopping worker gracefully...")
    finally:
        print("Worker stopped.")


# Requires a running Temporal server (`temporal server start-dev`)
if __name__ == "__main__":
    import asyncio

    print("Starting Temporal worker...")
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nExiting...")
