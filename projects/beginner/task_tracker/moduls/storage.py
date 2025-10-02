import json
from config import TASKS_FILE
#TODO: writer error handeler

def WriteFileJSON(input_data) :
    """
    write the file in json format
    
    parametr(s) : 
    ---------
    input_data : dic
    
    return(s) : 
    -------
    None
    """
    with open (TASKS_FILE,"w",enconding="utf-8") as f:
        json.dump(input_data , f, ensure_ascii=False,indent=4)  
                         
def ReadFileJSON ():
    """
    read the file and return to list format
    
    parametr(s):
    -----------
    None
    
    return(s):
    ---------
    data : list
    """
    with open (TASKS_FILE,"r") as f : 
        data =json.load(f)
        return data
    
# CRUD operations
    
def get_next_id():
    """
    this function read the file and find the last id in tasks, return the next id to use in creat task
    
    parametr(s):
    -----------
    None
    
    return(s):
    ---------
    next_id : int|
        the id for the creat the current task
    
    """
    data = ReadFileJSON()
    if not data:
        return 1
    max_id = max(item["ID"] for item in data)
    return max_id + 1

def save_data(task):
    """
    this function saving the current task in file
    
    parametr(s):
    -----------
    task : dic|
        the task was input
    
    return(s):
    --------
    None
    
    """
    data = ReadFileJSON()
    data.append(task)
    WriteFileJSON(data)
    

def update_data(updated_task):
    """
    this fonction save the updated task in file
    
    parametr(s):
    -----------
    updated_task: dic|
        the updated task
        
        
    return(s):
    ---------
    None
    
    """
    data = ReadFileJSON()
    for index, item in enumerate(data):
        if item["ID"] == updated_task["ID"]:
            data[index] = updated_task
            break
    WriteFileJSON(data)
    
def delete_data(task_id):
    """
    delete the chosen task in file
    
    parametr(s):
    --------
    task_id : str|
        the id of chosen task
        
    return(s):
    ---------
    None
    """
    
    data = ReadFileJSON()
    data = [item for item in data if item["ID"] != task_id] 
    WriteFileJSON(data)              
    
    