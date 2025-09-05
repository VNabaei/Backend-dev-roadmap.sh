"""
Lists Module
============

This module is responsible for managing **ToDo Lists** in the application and provides functions for:
    - Creating new lists
    - Managing CSV files associated with each list
    - Displaying, editing, and deleting lists
    - Checking the status of tasks and calculating the progress percentage of each list
    - Adding tasks and creating empty lists if needed

This module works together with other modules (`storage`, `utils`, `tasks`) and configuration files (`config`).

------------------------------
**Main Features of the Module**
------------------------------

1. **List File Management**
   - Creating a CSV file for each list
   - Generating a unique path if a file with the same name already exists
   - Deleting list files and updating the main table of lists

2. **Task Management**
   - Adding new tasks to the list
   - Displaying all active or completed tasks
   - Displaying tasks according to their deadline status (Expired, Due Today, Active)
   - Creating empty lists if no tasks exist

3. **Progress Reporting**
   - Calculating the progress percentage of each list
   - Displaying task statuses (Done, In Progress, Delayed, To Do)
   - Providing a colored progress bar for each list

------------------------------
**Used Modules**
------------------------------

- **os**:
  - Handles file paths and system operations
- **storage**:
  - Reading and writing CSV files
- **utils**:
  - Helper functions for path management, color formatting, and folder creation
- **tasks**:
  - Managing tasks and adding them to lists
- **config**:
  - Project constants like paths, column names, and colors

------------------------------
**Important Constants**
------------------------------

- `TABLE_LIST_PATH` : The path of the main table storing the lists.
- `APP_FOLDER_PATH` : The folder path for storing ToDo List files.
- `FIELDS_TASKS` : Fields related to each task.
- `FIELDS_TABLE` : Fields of the table storing the lists.
- `FILE_STATUS` : File statuses (Active, Deleted, etc.).
- `EXPIRED_COLOR`, `DUE_TODAY_COLOR`, `ACTIVE_COLOR` : Colors for task status display.
- `RESET_COLOR` : Reset color for terminal output.

------------------------------
**Main Functions**
------------------------------

### 1. `get_unique_filename(file_path)`
    - Input: File path
    - Output: Unique file path + counter
    - Description: If the file exists, generates a new name in the form `file(1).csv`, `file(2).csv`, etc.

---

### 2. `Create_New_list(title_list: str)`
    - Input: Title of the new list
    - Output: Path of the created file and list ID
    - Description:
        * If the list name already exists, the user chooses whether to replace it or create a unique file.
        * The CSV file is created and registered in the main table.
        * Tasks can be added immediately if desired.

---

### 3. `Show_List_ALLTask(file_path)`
    - Input: Path of the list file
    - Output: None
    - Description: Displays all tasks in the list with full details.

---

### 4. `show_All_lists()`
    - Input: None
    - Output: None
    - Description:
        * Displays all active lists along with their progress percentage.

---

### 5. `Show_List(file_path)`
    - Input: Path of the list file
    - Output: None
    - Description:
        * Displays the progress percentage and status of all tasks in the list with colors.
        * Tasks are grouped by deadline status:
            - **Expired** : Expired tasks
            - **Due Today** : Tasks due today
            - **Active** : Active tasks

---

### 6. `delete_List(file_path, tableListPath)`
    - Input: Path of the list file and main table path
    - Output: None
    - Description:
        * Deletes the CSV file of the list.
        * Removes the corresponding row from the main table.

---

### 7. `list_Status(file_path)`
    - Input: Path of the list file
    - Output: D



ماژول لیست وظایف 
============

این ماژول مسئول مدیریت **لیست‌های کار (ToDo Lists)** در برنامه است و شامل توابعی برای:
    - ساخت لیست‌های جدید
    - مدیریت فایل‌های CSV مرتبط با هر لیست
    - نمایش، ویرایش و حذف لیست‌ها
    - بررسی وضعیت تسک‌ها و درصد پیشرفت هر لیست
    - اضافه‌کردن تسک‌ها و ایجاد لیست‌های خالی در صورت نیاز

این ماژول به کمک سایر ماژول‌ها (`storage`, `utils`, `tasks`) و همچنین فایل‌های پیکربندی (`config`) کار می‌کند.

------------------------------
**امکانات اصلی ماژول**
------------------------------

1. **مدیریت فایل‌های لیست**
   - ایجاد فایل CSV برای هر لیست
   - تولید مسیر یکتا در صورت وجود فایل همنام
   - حذف فایل‌های لیست و بروزرسانی جدول اصلی لیست‌ها

2. **مدیریت تسک‌ها**
   - اضافه‌کردن تسک‌های جدید به لیست
   - نمایش تمام تسک‌های فعال یا کامل‌شده
   - نمایش تسک‌ها بر اساس وضعیت ددلاین (منقضی‌شده، امروز، فعال)
   - ایجاد لیست‌های خالی در صورت نبود تسک

3. **گزارش وضعیت**
   - محاسبه درصد پیشرفت هر لیست
   - نمایش وضعیت تسک‌ها (انجام‌شده، در حال انجام، معوقه، در انتظار شروع)
   - ارائه نمودار پیشرفت رنگی برای هر لیست

------------------------------
**ماژول‌های استفاده‌شده**
------------------------------

- **os**:
  - مدیریت مسیر فایل‌ها و عملیات سیستمی
- **storage**:
  - خواندن و نوشتن فایل‌های CSV
- **utils**:
  - توابع کمکی برای مدیریت مسیر، رنگ‌بندی و ساخت پوشه‌ها
- **tasks**:
  - مدیریت تسک‌ها و اضافه‌کردن آن‌ها به لیست‌ها
- **config**:
  - ثابت‌های پروژه مانند مسیرها، نام ستون‌ها و رنگ‌ها

------------------------------
**ثابت‌های مهم**
------------------------------

- `TABLE_LIST_PATH` : مسیر جدول اصلی که لیست‌ها را ذخیره می‌کند.
- `APP_FOLDER_PATH` : مسیر پوشه ذخیره‌سازی فایل‌های ToDo List.
- `FIELDS_TASKS` : فیلدهای مربوط به هر تسک.
- `FIELDS_TABLE` : فیلدهای جدول لیست‌ها.
- `FILE_STATUS` : وضعیت فایل‌ها (فعال، حذف‌شده و ...).
- `EXPIRED_COLOR`, `DUE_TODAY_COLOR`, `ACTIVE_COLOR` : رنگ‌های نمایشی وضعیت تسک‌ها.
- `RESET_COLOR` : ریست رنگ برای خروجی ترمینال.

------------------------------
**توابع اصلی**
------------------------------

### 1. `get_unique_filename(file_path)`
    - ورودی: مسیر فایل
    - خروجی: مسیر یکتای فایل + شمارنده
    - توضیح: اگر فایل موجود باشد، نام جدیدی به فرم `file(1).csv`, `file(2).csv` و ... تولید می‌کند.

---

### 2. `Create_New_list(title_list: str)`
    - ورودی: عنوان لیست جدید
    - خروجی: مسیر فایل ساخته‌شده و شناسه لیست
    - توضیح:
        * در صورت تکراری بودن نام لیست، کاربر برای جایگزینی یا ساخت فایل یکتا انتخاب می‌کند.
        * فایل CSV ایجاد شده و در جدول اصلی ثبت می‌شود.
        * امکان اضافه کردن تسک‌ها همان لحظه فراهم است.

---

### 3. `Show_List_ALLTask(file_path)`
    - ورودی: مسیر فایل لیست
    - خروجی: ندارد
    - توضیح: تمام تسک‌های لیست را با جزئیات کامل نمایش می‌دهد.

---

### 4. `show_All_lists()`
    - ورودی: ندارد
    - خروجی: ندارد
    - توضیح:
        * لیست تمام لیست‌های فعال را همراه با درصد پیشرفت نشان می‌دهد.

---

### 5. `Show_List(file_path)`
    - ورودی: مسیر فایل لیست
    - خروجی: ندارد
    - توضیح:
        * درصد پیشرفت و وضعیت تمام تسک‌های لیست را با رنگ‌بندی نمایش می‌دهد.
        * تسک‌ها بر اساس وضعیت ددلاین گروه‌بندی می‌شوند:
            - **Expired** : منقضی شده
            - **Due Today** : ددلاین امروز
            - **Active** : در حال انجام

---

### 6. `delete_List(file_path, tableListPath)`
    - ورودی: مسیر فایل لیست و مسیر جدول اصلی لیست‌ها
    - خروجی: ندارد
    - توضیح:
        * فایل CSV لیست حذف می‌شود.
        * ردیف مربوط به لیست از جدول اصلی پاک می‌شود.

---

### 7. `list_Status(file_path)`
    - ورودی: مسیر فایل لیست
    - خروجی: دیکشنری شامل اطلاعات زیر:
        * `Progress_percentage` : درصد پیشرفت
        * `ToDo` : تعداد تسک‌های در انتظار
        * `Done` : تعداد تسک‌های انجام‌شده
        * `In_progress` : تعداد تسک‌های در حال انجام
        * `Deleyed` : تعداد تسک‌های معوقه
        * `counter` : تعداد کل تسک‌ها
    - توضیح:
        * درصد پیشرفت بر اساس تسک‌های انجام‌شده محاسبه می‌شود.
        * اگر تسکی وجود نداشته باشد، مقدارها صفر برگردانده می‌شوند.

------------------------------
**نکات قابل توسعه**
------------------------------

- افزودن تابع `Update_List()` برای به‌روزرسانی عنوان لیست و تسک‌ها
- افزودن تابع `Edit_List()` برای ویرایش تسک‌های موجود
- اتصال به رابط کاربری گرافیکی برای مدیریت بهتر لیست‌ها

"""


from modules import storage,utils,tasks
import os
from config import TABLE_LIST_PATH,APP_FOLDER_PATH,FIELDS_TASKS,FIELDS_TABLE,FILE_STATUS,EXPIRED_COLORE,DUE_TODAY_COLOER,ACTIVE_COLORE,RESET_COLOR,WARNING_COLOR,ATTENTION_COLOR

#region : To Do List file creator : 
import os
import re

def get_unique_filename(file_path):
    """
    Create a unique file path by incrementing the number inside parentheses.
    For example:
    first.py -> first(1).py -> first(2).py -> first(3).py ...
    
    Parameters:
    -----------
    file_path : str
        Original file path
    
    Returns:
    --------
    new_file_path : str
        Unique file path
    counter : int
        Next counter used
    """
    directory, original_name = os.path.split(file_path)
    base, ext = os.path.splitext(original_name)

    # Match if name already has (number)
    match = re.match(r"^(.*?)(?:\((\d+)\))?$", base)
    name_base = match.group(1)
    
    counter = 0
    new_file_path = file_path

    while os.path.exists(new_file_path):
        counter += 1
        new_file_name = f"{name_base}({counter})"
        new_file_path = os.path.join(directory, f"{new_file_name}.{ext}")

    return new_file_path, new_file_name


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
        utils.Foulder_of_ToDoList_Creator ()

    file_path = os.path.join(APP_FOLDER_PATH,f"{title_list}.csv") # INFO : creat file path
    #INFO : Checks if the file already exists.
    if os.path.exists(file_path):
        #INFO : if exists
        ans = input (f"{ATTENTION_COLOR}this list is exists now!\nDo you want replace it ?(y/n){RESET_COLOR}") 
        if ans.upper() != 'y':
            #INFO : If the file is not replaced, the operation will stop.
            while os.path.exists(file_path):
                (file_path , title_list) = get_unique_filename(file_path)
                
            utils.Add_List_in_Table_list(title_list,file_path)
            storage.totalwrite_csv(file_path,FIELDS_TASKS)
        else : #INFO : If it wants to be replaced, the previous file path is deleted and a new path is created.
            delete_List(file_path)
            Create_New_list(title_list) 
    else :#INFO : if the file not exsist
        utils.Add_List_in_Table_list(title_list,file_path)
        storage.totalwrite_csv(file_path,FIELDS_TASKS)    
     
    # ---- If desired, the file will be completed.   
    
    #Add the tasks :
    ans =input("Do you want add tasks to this list (y/n)? : ")
    if ans.upper() == 'Y':
        reader = storage.read_csv(TABLE_LIST_PATH)
        for row in reader :
            if row.get("Title","") == title_list:
                 ToDoList_id = row.get("Id","")
       
        tasks.add_task(file_path,ToDoList_id)
    else:
        print("No tasks added to the list.")
        tasks.null_todolist_creator(file_path)
        
      
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
    print(f" ---- in {status_of_list['conter']} task(s)")
    print(f"|{status_of_list['Done']} task(S) was Done \n|{status_of_list['In_progress']} task(s) in progress \n|{status_of_list['ToDo']} task(s) To Do \n|{status_of_list['Deleyed']} task(s) is deleyed \n")
    print(" ---- Task status by deadline n")
    
    #TODO : نمایش تسک ها بر اساس تاخیر ددلاین 
    #the colors :
    
    print (f"{EXPIRED_COLORE}Expired{RESET_COLOR} :\n")
    
    print(list(row.get('Title') for row in tasks if utils.check_deadline_status(row.get("DeadLine"))== "Expired" ))
    # print("--------------------\n")
    print (f"\n{DUE_TODAY_COLOER}Due Today {RESET_COLOR}:\n")
    print(list (row.get('Title') for row in tasks if utils.check_deadline_status(row.get("DeadLine"))== "Due Today" ))
    # print("--------------------\n")
    print (f"\n{ACTIVE_COLORE}Active {RESET_COLOR}:\n")
    print(list(row.get('Title') for row in tasks if utils.check_deadline_status(row.get("DeadLine")) in ("Active","Due Today") ))

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
            if lst.get("Path") != file_path:
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
        check = row.get('Task_Status')
        conter += 1
        match check :
            case 'Todo' :
                ToDo_Conter += 1
            case 'Done':
                Done_Conter += 1
            case 'In_progress' :
                InProgress_conter += 1
            case 'Deleyed' :
                Deleyed_conter += 1
            # case _ :
            #     print("warning : check the status")
    try :
        Progress_percentage = (Done_Conter/conter)*100
        
        status = {
            "Progress_percentage" : Progress_percentage,
            "ToDo" : ToDo_Conter,
            "Done" : Done_Conter,
            "In_progress" : InProgress_conter,
            "Deleyed" : Deleyed_conter,
            "conter" : conter
            }
        return  status
    except :
        print("There is no defined task for this To Do list.")
        
        status = {
            "Progress_percentage" : 0,
            "ToDo" : ToDo_Conter,
            "Done" : Done_Conter,
            "In_progress" : InProgress_conter,
            "Deleyed" : Deleyed_conter,
            "Conter" : 0
            }
        
        return status
  
#endregion
  