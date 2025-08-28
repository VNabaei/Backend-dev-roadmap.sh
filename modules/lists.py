import storage 
import os
import utils
import tasks
from config import TABLE_LIST_PATH,BASE_DIR_PATH,APP_FOLDER_PATH,FIELDS_TASKS,FIELDS_TABLE

#region : To Do List file creator : 

def Create_New_list(title_list :str):
    '''
    This function creates a file in csv format so that it can be loaded into the database.
    
    Parameters
    ---------- 
    title_list : str
    The input_Title given to the toDOLIST
    
    Returns
    -------
    the path of File created
    
    '''
    
    # Creating folders for TDL files 
    if not os.path.exists(APP_FOLDER_PATH):
        utils.Foulder_of_ToDoList_Creator (title_list)
    else :
        utils.Add_List_in_Table_list(title_list)
        
    file_path = os.path.join(APP_FOLDER_PATH,f"{title_list}.csv") # INFO : creat file path

    
    #INFO : Checks if the file already exists.
    if os.path.exists(file_path):
        #INFO : if exists
        ans = input ("this list is exists now!\nDo you want replace it ?(y/n)") 
        if ans.upper() != 'y': #INFO : If the file is not replaced, the operation will stop.
            return
        else : #INFO : If it wants to be replaced, the previous file path is deleted and a new path is created.
            delete_List(file_path)
            Create_New_list(title_list) 
    else :#INFO : if the file not exsist
        storage.totalwrite_csv(file_path,FIELDS_TASKS)

        
     
    # ---- If desired, the file will be completed.   
    
    #Add the tasks :
    ans =input("Do you want add tasks to this list (y/n)? : ")
    if ans.upper() == 'Y':
        reader = storage.read_csv(TABLE_LIST_PATH)
        for row in reader :
            if row.get("Title","") == title_list:
                 ToDoList_id = row.get("Id","")
       
        tasks.Add_Task(file_path,ToDoList_id)
    else:
        print("No tasks added to the list.")
        tasks.Null_ToDoList_creator(file_path)
        
      
    # ---- File creation operation completed.
    print(f"List {title_list} created successfully at {file_path}")
    return file_path ,ToDoList_id 
#endregion        


# region : operation function 

# ----- showing :

def Show_List_ALLTask(file_path):

    '''
    Displays all tasks in full detail.
    
    Parametr(s) :
    -----------
    ToDoList_Path : path
    
    Return(s):
    ---------
    None
    
    '''
    
    if not os.path.exists(file_path):
        print(f"{file_path} does not exist.") 
        return
 
    reader = storage.read_csv(file_path)
    tasks = [row for row in reader if row.get("file_status", "").lower() != file_status[2]]
    if not tasks:
        print("no active task was found")
        return
    for task in tasks:
        print(f"Title: {task.get('Title', '')} |Descreaption: {task.get('Descreaption', '')} | Status: {task.get('Status', '')}| DeadLine: {task.get('DeadLine', '')} | Created at: {task.get('Created_at', '')}")
  
# ----- deleting :

def delete_List(file_path,tableListPath) :
    '''
    This function, given the given file address, deletes the file and also deletes its row from the list table.
    
    Parametr(s):
    -----------
    file_path : path
    the path of data file
    
    tableListPath :path
    the path of table list
    
    Return(s):
    ---------
    None
    '''
    
    if os.path.exists(file_path):
        os.remove(file_path)
        lists = storage.read_csv(tableListPath)

        rows = []
        for lst in lists :
            if lst.get("path") != file_path:
                rows.append(lst)
        try:
            storage.totalwrite_csv(TABLE_LIST_PATH,FIELDS_TABLE,rows)    
        except ValueError as error :
            print(f"The operation to remove a list from the todo list failed while rewriting the table list file. Error:{error}\n")
            
        print(f"{file_path} has been deleted successfully.")
    else:
        print(f"{file_path} does not exist.")    
  
#endregion
  