
# import os
import storage

def creat_list_done():
    tasks = storage.ReadFileJSON()
    return [t for t in tasks if t["Status"] == "done"]

def creat_list_inprogress():
    tasks =storage.ReadFileJSON()
    return [t for t in tasks if t["Status"] == "in_progress"]


def creat_list_notDone():
    tasks = storage.ReadFileJSON()
    return [t for t in tasks if t["Status"] != "done"]


def check_status(task_id):
    tasks = storage.ReadFileJSON()
    for task in tasks:
        if task["ID"] == task_id:
            return task["Status"]
    return None  #if the task not found

def get_user():
    #TODO: impot the user in the key of task
    pass

def find_task_by_id():
    pass