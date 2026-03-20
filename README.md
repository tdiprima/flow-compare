# Myflow: Workflow Orchestration

Side-by-side implementations of the same two-task sequential workflow across four Python orchestration frameworks.

## Choosing an Orchestration Tool Is Hard

Prefect, Celery, Dagster, and Temporal each solve workflow orchestration differently — different mental models, different deployment requirements, different tradeoffs. Reading documentation and blog posts only gets you so far. Until you've written the same workflow in each one and run it, the differences are abstract.

## The Same Workflow, Four Ways

`myflow` implements one simple pattern — run Task A, then Task B — in each framework. The tasks themselves do nothing interesting. That's the point. With business logic removed, what remains is pure orchestration: how you define tasks, how you wire them together, what infrastructure you need, and how you actually run them.

| Framework | File(s) | External Service |
|---|---|---|
| Prefect | `myflow_prefect.py` | None |
| Celery | `celery_den.py` + `celery_trigger.py` | Redis |
| Dagster | `dagster_den.py` | None (or Dagster UI) |
| Temporal | `temporal_cave.py` + `temporal_trigger.py` | Temporal server |

## Example: Temporal

Temporal separates the worker from the trigger. The workflow itself uses async/await:

```python
# temporal_cave.py — worker + workflow definition
@activity.defn
async def task_a() -> None:
    print("Task A complete")

@workflow.defn
class MyFlow:
    @workflow.run
    async def run(self) -> None:
        await workflow.execute_activity(task_a, schedule_to_close_timeout=timedelta(seconds=10))
        await workflow.execute_activity(task_b, schedule_to_close_timeout=timedelta(seconds=10))
```

```python
# temporal_trigger.py — fires the workflow
await client.execute_workflow(MyFlow.run, id="my-workflow", task_queue="my-queue")
```

## Usage

### Prerequisites

Install dependencies with [uv](https://github.com/astral-sh/uv):

```bash
uv sync
```

### Prefect

No external services required.

```bash
python src/myflow/myflow_prefect.py
```

### Celery

Requires Redis. On macOS with Homebrew:

```bash
./redisctl.sh up
```

Start the worker, then trigger tasks in a second terminal:

```bash
# Terminal 1
celery -A celery_den worker --loglevel=info

# Terminal 2
python src/myflow/celery_trigger.py
```

### Dagster

Run directly or open the Dagster UI:

```bash
# In-process
python src/myflow/dagster_den.py

# UI
dagster dev
```

### Temporal

Requires a running Temporal server:

```bash
# Terminal 1
temporal server start-dev

# Terminal 2 — start the worker
python src/myflow/temporal_cave.py

# Terminal 3 — trigger the workflow
python src/myflow/temporal_trigger.py
```

## Requirements

- Python 3.11+
- Redis (Celery only)
- Temporal CLI (Temporal only)

## Observations

Prefect seems to be perfect. 😌
