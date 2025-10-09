
# import os
import storage

def creat_list_done():
    tasks = storage.ReadFileJSON()
    return [t["Description"] for t in tasks if t["Status"] == "done"]

def creat_list_in_progress():
    tasks =storage.ReadFileJSON()
    return [t["Description"] for t in tasks if t["Status"] == "in_progress"]


def creat_list_todo():
    tasks = storage.ReadFileJSON()
    return [t["Description"] for t in tasks if t["Status"] == "todo"]

def creat_list(request= "all"):
    if (request == "all"):
        tasks = storage.ReadFileJSON()
        name_tasks = [t["Description"] for t in tasks]
        return name_tasks
    elif (request == "done"):
        return creat_list_done()
    elif (request == "todo"):
        return creat_list_todo()
    elif (request == "in-progress"):
        return creat_list_in_progress()
    else :
        return " ⚠️ No status flag provided. Use --in_progress or --done or --todo"

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