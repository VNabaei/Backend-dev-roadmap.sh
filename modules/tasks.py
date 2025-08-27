from datetime import datetime
from config import FIELDS_TASKS,FILE_STATUS,TASK_STATUS
from modules import storage,utils
# from modules.utils import get_user
import os

#region : Task creator :

# ----- task creator :
def add_task(file_path,todolist_id):
    tasks = storage.read_csv(file_path)
    while True :
        title = input("Enter task title (leave empty to finish):\n")
        if not title :
            break
        task = {
            "Id" :utils.ID_Generator(file_path,todolist_id),
            "Title"  : title,
            "Descreaption" : input("Add descreaption\n:"),
            "DeadLine" : utils.Deadline_Creator(),
            "Task_status" : TASK_STATUS[1],
            "Created_at" : datetime.today().date(),
            "Edited_by" : utils.Editor(),
            "Create_by" : utils.Get_User(),
            "File_status" :FILE_STATUS[0]
        }
        tasks.append(task)
    storage.write_csv(file_path,FIELDS_TASKS,tasks)
    print(f"task(s) saved in {file_path} successfully")
    
def null_todolist_creator(FIELDS_TASKS,file_path):
    
    storage.totalwrite_csv(file_path,FIELDS_TASKS)

#endregion

#region : operation function of task :

# ----- delete 
def delete_task(file_path,task_title) :
    '''
    This function changes the file status in the given task to "deleted".
    
    Parametrs :
    ---------
    file_path : path
    the addres of TDL file
    
    Task : str
    The task we want to delete
    
    Returns :
    -------
    None
    '''
    if not os.path.exists(file_path):
        print(f"{file_path} does not exist.")
        return
    else:
        tasks = storage.read_csv(file_path)
        task_found = False
        data = []
        for task in tasks:
            if  task['Title'].strip().lower() == task_title.strip().lower():
                # task['file_status'] = file_status[2] NOTE : The log will be recorded in the action record.
                #TODO : recorde the log
                task_found = True
            else :
                data.append(task)
                
        if not task_found :
            print(f"{task_title} not found")
            return
        try :
            storage.totalwrite_csv(file_path,FIELDS_TASKS,data)
        except ValueError as error :
            print(f"The task deletion operation failed while overwriting the file. Error: {error} \n")

# ----- Editing

def Edit_Task(file_path,task_title):
    '''
    Finds the desired task and changes the modifiable attributes
    and overwrites the file.
    
    Parametr(s):
    ------------
    file_path : path.
        path of todo list
    Task : str.
        the title of the task you want to edit
        
    Return(s):
    ----------
    None
    
    '''

    if not os.path.exists(file_path):
        print(f"{file_path} does not exist.")
        return   
    else:
        tasks = storage.read_csv(file_path)
        task_found = False
        
        for task in tasks:
            if task['Title'].strip().lower() == task_title.strip().lower():
                Show_the_task(file_path,task_title)
                quest = input('what the filed do you want chang? input number!!\n(1.Title 2.Descreaption 3.DeadLine 4.Status) ')
                match (quest):
                    case "1":
                        task['Title'] = input('enter the title\n:')
                    case "2":
                        task['Descreaption'] = input('enter the info\n:')
                    case "3" :
                        task['DeadLine'] = utils.Deadline_Creator()
                    case "4": 
                        i= input('enter the status (1.Done, 2.Todo, 3.In Progress): ')
                        task['Status'] = TASK_STATUS[int(i)-1]
                    case __ :
                        print("the input is wrong")
                        return
                        
                task['file_status'] = FILE_STATUS[1]
                task_found = True
        if not task_found :
            print(f"{task_title} not found")
            return
        try :
            storage.totalwrite_csv(file_path,FIELDS_TASKS,tasks)
            
        except ValueError as error :
             print(f"The task edit operation failed while overwriting the file. Error:{error}\n")


# ----- showing :
   
def Show_the_task(file_path,task_title):

    '''
    This function displays the desired task.
    Parametr(s):
    -----------
    file_path : path.
        the path of todo list
    task_title : str.
        the name of The task in question
    Return(s):
    ----------
    None
    '''
    if not os.path.exists(file_path):
        return
    tasks = storage.read_csv(file_path)
    target_task = [row for row in tasks if (row.get("Statusfile", "").lower() != "delete") and (row.get("title", "").strip().lower() == task_title.strip().lower())]
    for task in target_task:
            print(f"Title: {task.get('title', '')} |Descreaption: {task.get('Descreaption', '')} | Status: {task.get('Status', '')}DeadLine: {task.get('DeadLine', '')} | Created at: {task.get('Created_at', '')} ")

#endrigion