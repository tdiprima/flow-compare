"""
run_all_mys.py 🧸
------------------------------------
Runs all available workflow POCs from Myflow.

Detects which frameworks are installed and runs their
respective demo scripts if possible.

Usage:
    python run_all_mys.py
"""

import importlib
import subprocess
import sys
from pathlib import Path

# 🐻 registry of workflow demos
DEMO_SCRIPTS = {
    "prefect": "myflow_prefect.py",
    # "celery": "celery_den.py",
    "dagster": "pipeline_paws.py",
    # "temporalio": "temporal_cave.py",
}


def check_module(module_name: str) -> bool:
    """Return True if module is installed."""
    try:
        importlib.import_module(module_name)
        return True
    except ImportError:
        return False


def run_script(script_name: str):
    """Run a script in a subprocess."""
    print(f"\n🚀 Running: {script_name}")
    script_path = Path(__file__).parent / script_name
    if not script_path.exists():
        print(f"⚠️  Missing script: {script_name}, skipping.")
        return
    try:
        subprocess.run([sys.executable, str(script_path)], check=True)
        print(f"✅ Finished: {script_name}")
    except subprocess.CalledProcessError:
        print(f"❌ Error running {script_name}")


def main():
    print("\n🧸 Myflow Workflow Launcher\n-----------------------------")
    available = []

    for mod, script in DEMO_SCRIPTS.items():
        if check_module(mod):
            available.append((mod, script))
        else:
            print(f"⏭️  Skipping {mod} (not installed)")

    if not available:
        print("\n😴 No frameworks installed. Try:\n")
        print("   uv add prefect celery dagster apache-airflow temporalio redis\n")
        return

    print("\n🐻 Available frameworks:")
    for mod, script in available:
        print(f" - {mod} → {script}")

    print("\n🔥 Starting demo runs...\n")
    for mod, script in available:
        run_script(script)

    print("\n✨ All done! My approves 🐾\n")


if __name__ == "__main__":
    main()
