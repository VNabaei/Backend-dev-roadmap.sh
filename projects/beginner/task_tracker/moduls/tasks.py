#Add, Update, and Delete tasks
import storage
import config
import datetime

def add_task(description,status="todo"):
    task_id = storage.get_next_id(config.TASKS_FILE)
    task = {
        "ID": task_id,
        "Description": description,
        "Status": status,
        "CreateAt": datetime.datetime.now().isoformat(),
        "UpdatedAt": None
    }
    storage.save_data(config.TASKS_FILE, task)
    
    return task

    
def update_task(task,description,status):
    updated_task = {
        "ID": task["ID"],
        "Description": description,
        "Status": status,
        "CreateAt": task["CreateAt"],
        "UpdatedAt": datetime.datetime.now().isoformat()
    }
    storage.update_data(config.TASKS_FILE, updated_task)
def delete_task(task):
    storage.delete_data(config.TASKS_FILE, task["ID"])
    
def mark(task,in_progress = False, done = False):
    if in_progress:
        new_status = "in_progress"
    elif done :
        new_status = "done"
    else :
         print("No status flag provided. Use --in_progress or --done.")        
         return
    
    return update_task(task,description=task["Description"],status=new_status)