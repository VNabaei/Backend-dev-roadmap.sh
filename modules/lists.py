import storage 
import os
import utils
import tasks
from config import TABLE_LIST_PATH,APP_FOLDER_PATH,FIELDS_TASKS,FIELDS_TABLE,FILE_STATUS

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
    tasks = [row for row in reader if row.get("file_status", "").lower() != FILE_STATUS[2]]
    if not tasks:
        print("no active task was found")
        return
    for task in tasks:
        print(f"Title: {task.get('Title', '')} |Descreaption: {task.get('Descreaption', '')} | Status: {task.get('Status', '')}| DeadLine: {task.get('DeadLine', '')} | Created at: {task.get('Created_at', '')}")

def show_All_lists():
    '''
    This function displays the Table list values
    
    Parametr(s) :
    --------
    None
    
    Return(s) :
    --------
    None
    '''
     
    try :
        lists = storage.read_csv(TABLE_LIST_PATH)    

        active_lists = [lst for lst in lists if lst.get("file_status") != FILE_STATUS[2]]
        if not active_lists:
            print("No active lists available.")
            return
        print("the title of active Lists : \n")
        for lst in active_lists:
            status_of_list =list_Status(lst.get('Path'))
            Progress_percentage = status_of_list['Progress_percentage']
            print(f" --> Title : {lst.get('Title',)} | Progress percentage : {utils.colored_progress_bar(Progress_percentage)}")    
    except ValueError as error :
        print(f"The operation to show the todo list failed. Error:{error}\n")

def Show_List(file_path):
    '''
    this function show the all task in todo list
    Details displayed:
    "Title","Descreaption","Status","Dead line" & "Created at" of the tasks in todo list
    
    Parametr(s):
    -----------
    ToDoList_Path : path
    
    Return(s):
    ---------
    None
    '''
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} does not exist.")

    reader = storage.read_csv(file_path)
    tasks = [row for row in reader if row.get("File_status", "").lower() != FILE_STATUS[2]]
    #TODO : show status in tasks
                
    status_of_list = list_Status(file_path)
    Progress_percentage = status_of_list['Progress_percentage']
    if not tasks:
        print("no active task was found")
        return
    print("in this To Do lists :\n")
    print(f"Progress percentage :  {utils.colored_progress_bar(Progress_percentage)}\n")
    print("-------------------------")
    print(f"{status_of_list['Done']} task(S) was Done \n|{status_of_list['In_progress']} task(s) in progress \n|{status_of_list['ToDO']} task(s) To Do \n|{status_of_list['Deleyed']} task(s) is deleyed \n")
    print("Task status by deadline -------------------------\n")
    
    #TODO : نمایش تسک ها بر اساس تاخیر ددلاین 
    #the colors :
    colorExpired = "\033[91m" 
    colorDue_Today = "\033[93m"
    colorActive = "\033[92m"
    reset = "\033[0m"
    
    print (f"{colorExpired}Expired{reset} :\n")
    
    print(list(row.get('Title') for row in tasks if utils.check_deadline_status(row.get("DeadLine"))== "Expired" ))
    # print("--------------------\n")
    print (f"\n{colorDue_Today}Due Today {reset}:\n")
    print(list (row.get('Title') for row in tasks if utils.check_deadline_status(row.get("DeadLine"))== "Due Today" ))
    # print("--------------------\n")
    print (f"\n{colorActive}Active {reset}:\n")
    print(list(row.get('Title') for row in tasks if utils.check_deadline_status(row.get("DeadLine"))== "Active" ))

    print("-----------------------------------------------------------------------")
   
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

def Update_List():
    #TODO : in progress
    pass  

def Edit_List ():
    #TODO : In progress
    pass

def list_Status(file_Path):
    '''
    Parametr(s):
    ------------
    file_path :str
    
    Return(s):
    ---------
    Progress_percentage : float
    ToDo_Conter : float
    Done_Conter : float
    InProgress_conter : float
    Deleyed_conter : float
    
    
    '''
    if not os.path.exists(file_Path):
        print(f"the path of {file_Path} not find")
        return 
    reader = storage.read_csv(file_Path)

    tasks = [row for row in reader if row.get("file_status", "").lower() != FILE_STATUS[2]]
    #TODO : show status in tasks
    ToDo_Conter = 0
    Done_Conter = 0 
    InProgress_conter = 0
    Deleyed_conter = 0
    conter = 0
    for row in tasks :
        check = row.get('Status')
        conter += 1
        match check :
            case 'Todo' :
                ToDo_Conter += 1
            case 'Done':
                Done_Conter += 1
            case 'In Progress' :
                InProgress_conter += 1
            case 'Deleyed' :
                Deleyed_conter += 1
            case _ :
                print("warning : check the status")
    try :
        Progress_percentage = (Done_Conter/conter)*100
        
        status = {
            "Progress_percentage" : Progress_percentage,
            "ToDo" : ToDo_Conter,
            "Done" : Done_Conter,
            "In_progress" : InProgress_conter,
            "Deleyed" : Deleyed_conter
            }
        return  status
    except :
        print("There is no defined task for this To Do list.")
        
        status = {
            "Progress_percentage" : 0,
            "ToDo" : ToDo_Conter,
            "Done" : Done_Conter,
            "In_progress" : InProgress_conter,
            "Deleyed" : Deleyed_conter
            }
        
        return status
  
#endregion
  