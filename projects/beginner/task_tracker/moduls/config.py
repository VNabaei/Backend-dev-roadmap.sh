# moduls/config.py
import os
from pathlib import Path
import sys

TASK_KEY_DEC = ["ID","Description","Status","CreateAt","UpdatedAt"]
TASK_STATUS = ["todo","in-progress","done"]

# def init_paths():
#     """initialize main paths for data and tasks file"""
#     run_file_path = Path(sys.argv[0]).resolve()
#     run_dir = run_file_path.parent

#     data_dir = run_dir / "data"
#     data_dir.mkdir(exist_ok=True)

#     tasks_file = data_dir / "tasks.json"

#     return run_file_path, run_dir, data_dir, tasks_file

TASKS_DIR = "D:\\roadMap\\Backend\\projects\\beginner\\task_tracker\\data"
TASKS_FILE =TASKS_DIR+"\\Tasks.json"