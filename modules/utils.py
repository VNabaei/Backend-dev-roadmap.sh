"""
Utils Module
=============

This module handles file management and basic operations related to **ToDo Lists**.

It includes functions for:
    - Creating and managing folders and the main table of lists
    - Getting IDs of lists and tasks
    - Checking the deadline status of tasks
    - Generating colored progress bars
    - Retrieving the operating system user

This module interacts with other modules (`storage`) and the configuration file (`config`).

------------------------------
Main Features
------------------------------

1. Folder and Table Management
   - `Add_List_in_Table_list(todolist_title, todolist_path)` : Adds a list entry to the main table
   - `Foulder_of_ToDoList_Creator(todolist_title)` : Creates the application folder and initializes the list table

2. Deadline Management
   - `Deadline_Creator()` : Prompts user for a valid future date in `YYYY/MM/DD` format. Defaults to today if empty.
   - `task_deadline_status(deadline_str)` : Returns task status based on its deadline ("Active", "Due Today", "Expired").
   - `check_deadline_status(deadline_str)` : Checks multiple date formats and returns task status

3. ID Generation
   - `ID_Generator(TodoList_Path, ToDoList_ID)` : Generates a unique Task ID in the format `TDL-{TDL_ID}-TSK-{YYYYMMDDHHMMSS}{counter}`

4. User Handling
   - `Editor()` : Returns the current user editing a task
   - `Get_User()` : Gets the username from the operating system

5. File & Path Utilities
   - `getPath(list_select)` : Returns the path of a ToDoList from the main table
   - `getId(list_Title, task_title=None)` : Returns the ID of a ToDoList or a specific task
   - `getTodolistId(todolist_path, title_list)` : Returns the ToDoList ID from the list file

6. Progress Visualization
   - `colored_progress_bar(percent, length=30)` : Returns a colored progress bar representing completion percentage

------------------------------
Important Constants
------------------------------

- `TABLE_LIST_PATH` : Path to the main table storing lists
- `APP_FOLDER_PATH` : Folder for ToDoList files
- `FIELDS_TABLE` : Columns for the main table
- `FILE_STATUS` : Status of lists (Active, Deleted, etc.)

------------------------------
Function Details
------------------------------

- `Add_List_in_Table_list(todolist_title, todolist_path)` : Adds a new list entry to the main table with ID, creator, creation date, and file path
- `Foulder_of_ToDoList_Creator(todolist_title)` : Creates the main application folder and initializes the list table with the given list title
- `Deadline_Creator()` : Prompts the user for a valid future date; defaults to today if input is empty
- `ID_Generator(TodoList_Path, ToDoList_ID)` : Generates a unique ID for each task in a ToDoList
- `Editor()` : Returns the user who edits a task
- `task_deadline_status(deadline_str)` / `check_deadline_status(deadline_str)` : Determines the status of a task
- `colored_progress_bar(percent, length=30)` : Creates a visual colored progress bar proportional to completion percentage
- `Get_User()` : Retrieves the current system user or returns "Unknown"
- `getPath(list_select)` : Returns the file path of a selected ToDoList
- `getId(list_Title, task_title=None)` : Returns the ID of the list or a specific task
- `getTodolistId(todolist_path, title_list)` : Returns the ToDoList ID from a given list file

------------------------------
Notes
------------------------------

- All dates are managed in `YYYY/MM/DD` format
- Task IDs are unique per ToDoList
- This module is tightly coupled with `storage` for CSV read/write operations
- Functions include input validation to prevent incorrect dates or paths

ماژول utils
=============

این ماژول مسئول مدیریت فایل‌ها و عملیات پایه‌ای مرتبط با **لیست‌های کار (ToDo Lists)** است.

شامل توابعی برای:
    - ایجاد و مدیریت پوشه‌ها و جدول اصلی لیست‌ها
    - دریافت شناسه لیست و تسک‌ها
    - بررسی وضعیت ددلاین تسک‌ها
    - تولید نوار پیشرفت رنگی
    - دریافت کاربر سیستم عامل

این ماژول با سایر ماژول‌ها (`storage`) و فایل پیکربندی (`config`) تعامل دارد.

------------------------------
امکانات اصلی
------------------------------

1. مدیریت پوشه و جدول
   - `Add_List_in_Table_list(todolist_title, todolist_path)` : اضافه کردن رکورد لیست به جدول اصلی
   - `Foulder_of_ToDoList_Creator(todolist_title)` : ایجاد پوشه اصلی برنامه و مقداردهی اولیه جدول لیست‌ها

2. مدیریت ددلاین
   - `Deadline_Creator()` : گرفتن تاریخ معتبر آینده از کاربر با فرمت `YYYY/MM/DD`. در صورت عدم وارد کردن، تاریخ امروز انتخاب می‌شود.
   - `task_deadline_status(deadline_str)` : وضعیت تسک را بر اساس ددلاین برمی‌گرداند ("Active", "Due Today", "Expired")
   - `check_deadline_status(deadline_str)` : بررسی چندین فرمت تاریخ و تعیین وضعیت تسک

3. تولید شناسه
   - `ID_Generator(TodoList_Path, ToDoList_ID)` : تولید شناسه یکتا برای هر تسک با فرمت `TDL-{TDL_ID}-TSK-{YYYYMMDDHHMMSS}{counter}`

4. مدیریت کاربر
   - `Editor()` : کاربر فعلی که تسک را ویرایش می‌کند را برمی‌گرداند
   - `Get_User()` : دریافت نام کاربر از سیستم عامل

5. ابزارهای مسیر و فایل
   - `getPath(list_select)` : مسیر فایل لیست انتخابی را از جدول اصلی برمی‌گرداند
   - `getId(list_Title, task_title=None)` : شناسه لیست یا تسک مشخص را برمی‌گرداند
   - `getTodolistId(todolist_path, title_list)` : شناسه لیست را از فایل لیست برمی‌گرداند

6. نمایش پیشرفت
   - `colored_progress_bar(percent, length=30)` : نوار پیشرفت رنگی متناسب با درصد پیشرفت ایجاد می‌کند

------------------------------
ثابت‌های مهم
------------------------------

- `TABLE_LIST_PATH` : مسیر جدول اصلی لیست‌ها
- `APP_FOLDER_PATH` : پوشه ذخیره‌سازی فایل‌های ToDo List
- `FIELDS_TABLE` : ستون‌های جدول اصلی
- `FILE_STATUS` : وضعیت فایل‌ها (فعال، حذف‌شده و ...)

------------------------------
جزئیات توابع
------------------------------

- `Add_List_in_Table_list(todolist_title, todolist_path)` : اضافه کردن رکورد جدید به جدول اصلی با اطلاعات: ID، سازنده، تاریخ ایجاد و مسیر فایل
- `Foulder_of_ToDoList_Creator(todolist_title)` : ایجاد پوشه اصلی برنامه و مقداردهی اولیه جدول لیست‌ها
- `Deadline_Creator()` : گرفتن تاریخ معتبر آینده از کاربر؛ در صورت عدم وارد کردن، تاریخ امروز برگردانده می‌شود
- `ID_Generator(TodoList_Path, ToDoList_ID)` : تولید شناسه یکتا برای هر تسک
- `Editor()` : بازگرداندن کاربر ویرایشگر تسک
- `task_deadline_status(deadline_str)` / `check_deadline_status(deadline_str)` : تعیین وضعیت تسک
- `colored_progress_bar(percent, length=30)` : ایجاد نوار پیشرفت رنگی متناسب با درصد تکمیل
- `Get_User()` : دریافت کاربر فعلی سیستم یا "Unknown"
- `getPath(list_select)` : برگرداندن مسیر فایل لیست انتخاب شده
- `getId(list_Title, task_title=None)` : برگرداندن شناسه لیست یا تسک مشخص
- `getTodolistId(todolist_path, title_list)` : برگرداندن شناسه لیست از فایل مربوطه

------------------------------
نکات و توصیه‌ها
------------------------------

- تمام تاریخ‌ها با فرمت `YYYY/MM/DD` مدیریت می‌شوند
- شناسه تسک‌ها به‌صورت یکتا برای هر لیست تولید می‌شوند
- این ماژول به `storage` برای خواندن و نوشتن CSV وابسته است
- توابع شامل اعتبارسنجی ورودی برای جلوگیری از ورود داده اشتباه هستند
"""

from datetime import datetime,date
import os
import getpass
from modules import storage
from config import TABLE_LIST_PATH,APP_FOLDER_PATH,FIELDS_TABLE,FILE_STATUS

#region : the functions 
# -------------------------------------------------------------
#Folder Handeller :
def Add_List_in_Table_list(todolist_title,todolist_path):
    try :
            reader = storage.read_csv(TABLE_LIST_PATH)
            
            data =[
                {
                    'Id':datetime.today().strftime("%Y%m%d%H%M%S")
                    ,'Title' : todolist_title
                    ,'Creator' : Get_User()
                    ,'Created_at' : datetime.today()
                    ,'File_status' : FILE_STATUS[0]
                    ,'Path' : todolist_path # INFO : creat file path #INFO : We need this to check the to do list ID
                }
                ]
            
            reader.extend(data)
    except ValueError as error :
        print(f"The operation to create the lists table failed. Error: {error}\n")
        
    try :  
        storage.totalwrite_csv(TABLE_LIST_PATH,FIELDS_TABLE,reader)  

    except ValueError as error :
        print("error in csv file : dict contains fields not in fieldnames")
        
        
# -------------------------------------------------------------
# FolderCreator :
def Foulder_of_ToDoList_Creator (todolist_title):
        os.makedirs(APP_FOLDER_PATH)
         #INFO : creat path 
        #INFO : Create a table containing list information    
        data = [
            {
                'Id':datetime.today().strftime("%Y%m%d%H%M%S")
                ,'Title' : todolist_title
                ,'Creator' : Get_User()
                ,'Created_at' : datetime.today()
                ,'File_status' : FILE_STATUS[0]
                ,'Path' : os.path.join(APP_FOLDER_PATH,f"{todolist_title}.csv") #INFO : We need this to check the to do list ID
            }
         ]
        try : 
            storage.totalwrite_csv(TABLE_LIST_PATH,FIELDS_TABLE,data)
        except ValueError as error:
            print(f"The operation to create the Folder of todo lists failed. Error: {error}\n")
            

#endregion    


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

def task_deadline_status(deadline_str):
    """
    Returns the status of a task based on its deadline.
    
    Parameters:
    -----------
    deadline_str : str
        Deadline in 'YYYY/MM/DD' format

    Returns:
    --------
    str : "Active", "Due Today", or "Expired"
    """
    try:
        deadline_date = datetime.strptime(deadline_str, "%Y/%m/%d").date()
        today = datetime.today().date()
        if deadline_date < today:
            return "Expired"
        elif deadline_date == today:
            return "Due Today"
        else:
            return "Active"
    except Exception:
        return "Unknown situation in deadline calculate"


def check_deadline_status(deadline_str: str) -> str:
    """
    Checks the status of a task based on its deadline.
    Accepts 'M/D/YYYY', 'MM/DD/YYYY', 'YYYY/MM/DD', or 'YYYY-M-D' formats.

    Returns: "Expired", "Due Today", "Active", or "Invalid Format"
    """
    if not deadline_str or deadline_str.strip() == "":
        return "Invalid Format"

    # لیست فرمت‌های ممکن
    possible_formats = ["%m/%d/%Y", "%Y/%m/%d", "%Y-%m-%d"]

    for fmt in possible_formats:
        try:
            deadline_date = datetime.strptime(deadline_str.strip(), fmt).date()
            today = datetime.today().date()

            if deadline_date < today:
                return "Expired"
            elif deadline_date == today:
                return "Due Today"
            else:
                return "Active"
        except ValueError:
            continue

    return "Invalid Format"                

def colored_progress_bar(percent: float, length: int = 30) -> str:
    """
    This function displays a colored progress bar in proportion to the percentage of progress.
     
    Parameter(s):
    -----------
    percent : float
        درصد پیشرفت (۰ تا ۱۰۰)
    length : int
        طول نوار پیشرفت (پیش‌فرض ۳۰ کاراکتر)

    Return(s):
    --------
    str : نوار پیشرفت رنگی همراه با درصد
    """

    # محدود کردن درصد بین 0 و 100
    percent = max(0, min(100, percent))

    # محاسبه‌ی بلوک‌های پر و خالی
    filled_length = int(length * percent // 100)
    empty_length = length - filled_length

    # انتخاب رنگ با ANSI escape codes
    if percent < 40:
        color = "\033[91m"   # قرمز
    elif percent < 80:
        color = "\033[93m"   # زرد
    else:
        color = "\033[92m"   # سبز

    reset = "\033[0m"
    bar = f"{color}{'█' * filled_length}{reset}{'-' * empty_length}"

    return f"[{bar}] {percent}%"


# Get Function :
#----------------------------------------------------------------------
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


def getPath(list_select : str):
    '''
    This function finds the address of the To Do List from the table list.
    
    Parametr(s) :
    -----------
    list_select : str
    the Title of to do list or task
    
    Return(s) :
    ---------
    path
    
    '''
    reader = storage.read_csv(TABLE_LIST_PATH)
    for row in reader:
        chosen_list = list_select.strip().lower()
        if row.get('Title', '').strip().lower() == chosen_list :
            return row.get('Path')
    return None 

def getId(list_Title: str, task_title: str = None):
    '''
    This function returns ID of either a ToDoList or a Task.
    
    Parameters
    ----------
    list_Title : str
        Title of the ToDoList
    task_title : str, optional
        Title of the task (if provided, returns Task ID instead of List ID)
    
    Returns
    -------
    str or None
        ID of the ToDoList or Task
    '''
    
    # search in lists
    reader = storage.read_csv(TABLE_LIST_PATH)

    for row in reader:
        if row.get("Title") == list_Title:
            list_id = row.get("Id")
            list_path = row.get("Path")
                
                #just for list
            if task_title is None:
                return list_id
                
                # Just for task selected
            if os.path.exists(list_path):
                task_reader = storage.read_csv(list_path)
                for task in task_reader:
                    if task.get("Title", "").strip().lower() == task_title.strip().lower():
                        return task.get("Id")
            else:
                    
                return None
    
    return None
def getTodolistId(todolist_path,title_list) :
    reader = storage.read_csv(todolist_path) 
    for row in reader :
        if row.get("Title","") == title_list:
            ToDoList_id = row.get("Id","")
            return ToDoList_id
    print(f"{Warning}{title_list} not found!")

#endregion   