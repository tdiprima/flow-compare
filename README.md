# 🐻 Myflow: Workflow Orchestration

This repo is for exploring different **workflow management systems**.

It's not production. It's **proof-of-concept**.

## 🗺️ What's Inside

Each folder/file is a tiny POC showing a 2-task workflow:

Task A → Task B → "Flow complete!"

| Framework | Filename |
|------------|-----------|
| 🌀 **Prefect** | `myflow_prefect.py` |
| ⚙️ **Celery** | `celery_den.py` |
| 🧩 **Dagster** | `dagster_den.py` |
| ⏳ **Temporal** | `temporal_cave.py` |

## 🧰 Setup

If you're using [`uv`](https://github.com/astral-sh/uv) (and you should), grab the dependencies you need:

### Install them all

```bash
uv sync
# or
uv add prefect celery dagster temporalio redis
```

## 🧪 Running the POCs

Each script can be run locally:

### Prefect

```bash
uv run myflow_prefect.py
```

### Celery

```bash
# Terminal A: start redis
./redisctl.sh up
# Or
redis-server

# Terminal 1: start worker
celery -A celery_den worker --loglevel=info

# Terminal 2: trigger tasks
uv run celery_trigger.py
```

### Dagster

```bash
uv run dagster_den.py
```

### Temporal

```bash
# Terminal 1: Start Temporal server
temporal server start-dev

# Terminal 2: Run the worker
uv run temporal_cave.py

# Terminal 3: Trigger the workflow
uv run temporal_trigger.py
```

## 🪄 Future Ideas

* Add async workflows for Celery & Prefect
* Compare logging/monitoring tools (Prefect Cloud vs Dagit vs Temporal UI)
* Dockerize everything for local orchestration lab

## 🐻 Closing Thoughts

Prefect seems to be perfect.

<br>
