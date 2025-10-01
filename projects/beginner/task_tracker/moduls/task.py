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
    
    # return task

    pass
def update_task(self,description,status):
    updated_task = {
        "ID": self["ID"],
        "Description": description,
        "Status": status,
        "CreateAt": self["CreateAt"],
        "UpdatedAt": datetime.datetime.now().isoformat()
    }
    storage.update_data(config.TASKS_FILE, updated_task)
def delete_task(self):
    storage.delete_data(config.TASKS_FILE, self["ID"])
    pass
    