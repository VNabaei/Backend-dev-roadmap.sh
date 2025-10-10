import json
import os
from config import TASKS_DIR,TASKS_FILE

#TODO: writer error handeler
#NOTE : the address was defide, if the path changed, change the code!!!


# FIX IT :
# def init_storage(task_path):
#     global TASKS_FILE 
#     TASKS_FILE = task_path
# TASKS_FILE = 


# در ابتدای هر ماژول
if __name__ == "__main__":
    
    raise RuntimeError("run the main program")

# pass path :
   
def WriteFileJSON(input_data) :
    """
    write the file in json format
    
    parameter(s) : 
    ---------
    input_data : dic
    
    return(s) : 
    -------
    None
    
    """
    try : 
        with open (TASKS_FILE,"w",encoding="utf-8") as f:
            json.dump(input_data , f, ensure_ascii=False,indent=4)  
        print(" task was creat successfull")
    except ValueError as e :
        raise  e
                     
def ReadFileJSON ():
    """
    read the file and return to list format
    
    parameter(s):
    -----------
    None
    
    return(s):
    ---------
    data : list
    """
    if not os.path.exists(TASKS_FILE):
        # print("no tasks was found")
        return []
      
    
    with open (TASKS_FILE,"r") as f : 
        data =json.load(f)
        return data
    
# CRUD operations
    
def get_next_id():
    """
    this function read the file and find the last id in tasks, return the next id to use in creat task
    
    parameter(s):
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
    
    parameter(s):
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
    
    parameter(s):
    -----------
    updated_task: dic|
        the updated task
        
        
    return(s):
    ---------
    None
    
    """
    data = ReadFileJSON()
    if data != [] :
        
        for index, item in enumerate(data):
            if item["ID"] == updated_task["ID"]:
                data[index] = updated_task
                break
            else :
                print ("the task wasn't found")
        WriteFileJSON(data)
    else :
        print("no tasks was found")
    
def delete_data(task_id):
    """
    delete the chosen task in file
    
    parameter(s):
    --------
    task_id : str|
        the id of chosen task
        
    return(s):
    ---------
    None
    """
    
    data = ReadFileJSON()
    data = [item for item in data if item["ID"] != int(task_id)] 
    WriteFileJSON(data)              
    
    