import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

TASKS_FILE = os.path.join(DATA_DIR, "tasks.json")

TASK_KEY_DEC = ["ID","Description","Status","CreateAt","UpdatedAt"]
TASK_STATUS = ["todo","in-progress","done"]