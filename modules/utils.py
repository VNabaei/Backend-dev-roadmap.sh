from datetime import datetime,date
import getpass
import storage

def Deadline_Creator():
    '''
    It takes a date from the user and checks that its format is Y /MM /DD. And the date is in the future. If the user does not enter a date, it outputs the date of that day.
    This operation continues until the user enters valid data.

    Parametr(s):
    ------------
    None
    
    Return(s):
    ----------
    date : str.
        in YY/MM/DD format
    today's date : str
        when the user input noting
        
    '''
    while True:
        ddline_input = input("inter the DDline (Year/month/day) e.g. : 2025/07/31  : ") 
        if ddline_input :
            try:
                ddline_date = datetime.strptime(ddline_input, "%Y/%m/%d").date()
                if ddline_date < datetime.today().date():
                    print("DDline can not be in pass")
                    continue
                else:
                    return ddline_date
                    
            except ValueError:
                print("the format is wrong")
                print("Please enter the date in the format Y/M/D (e.g.: 2025/07/31)")
                continue
            break #exit the loop if date is valid
        else:
            ddline_date = datetime.today().date()
            print("DDline is set to today")
            return ddline_date
            break #exit the loop if no date is provided

def ID_Generator(TodoList_Path,ToDoList_ID) :
    #TODO : Optimize
    '''
    This function get the last id and creat the next id 
    
    Parametr(s) : 
    -------------
    TodoList_Path : path.
        the path of table list
    ToDoList_ID : str
        the ID of current todo list 
    
    Return(s):
    ----------
    Task ID : str
        ID format : TDL - {TDL_ID} - TSK - {YYYYMMDDHHMMSS} + {counter of tasks in this TDL file}

    '''
    rows = storage.read_csv(TodoList_Path)
    if rows:
        last_row = rows[-1]
        id = last_row["Id"]
     
        x = int(id[43:]) #NOTE : It only works for this ID format. 
        x += 1
            
            #region : for optimize-----------------
            #NOTE : There is another way to separate the counter section, but I am not using it right now.
            # match = re.search(r'(\d+)$', id)  # آخرین عدد رو می‌گیره
            # if match:
            #     x = int(match.group(1)) + 1
            # else:
            #     x = 1
            #endregion        
    else :
        x = 0
    return f'TDL - {ToDoList_ID} - TSK - {datetime.today().strftime("%Y%m%d%H%M%S")}'+ f'{x:03d}'
    #NOTE : ID format : TDL - {TDL_ID} - TSK - {YYYYMMDDHHMMSS} + {counter of tasks in this TDL file}
    #review : ID is too long, sorry.

def Editor():
    '''
    this function get user when the edit function called
    
    Parametr(s):
    ---------
    null
    
    Return(s):
    -------
    the user that editied the TDL/TSK
    '''
    return Get_User()

def Get_User():
    '''
    Getting User from operation system
    
    Parametr(s):
    ------------
    None
    
    Return(s):
    ----------
    user or Unknown :str
    '''
    try:
        user = getpass.getuser()
        return user
    except Exception:
        return "Unknown"
