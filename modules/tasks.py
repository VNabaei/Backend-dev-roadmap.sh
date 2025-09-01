"""
Task Module
=============

This module manages **tasks** within ToDo Lists.

It provides functions for:
    - Adding new tasks
    - Creating empty ToDoList files
    - Editing and deleting tasks
    - Displaying tasks with details

The module interacts with `storage` for CSV operations and `utils` for helper functions such as ID generation, deadline creation, and user retrieval.

------------------------------
Main Features
------------------------------

1. Task Creation
   - `add_task(file_path, todolist_id)` : Adds tasks to a ToDoList file
   - `null_todolist_creator(file_path)` : Creates an empty ToDoList file

2. Task Operations
   - `delete_task(file_path, task_title)` : Marks a task as deleted in the CSV file
   - `Edit_Task(file_path, task_title)` : Edits attributes of a task and updates the file
   - `Show_the_task(file_path, task_title)` : Displays detailed information of a task

3. Utilities
   - Interacts with `utils.ID_Generator` for unique task IDs
   - Uses `utils.Deadline_Creator` for deadline input
   - Uses `utils.Editor` and `utils.Get_User` to track who edits or creates tasks
   - Works with constants like `FIELDS_TASKS`, `FILE_STATUS`, and `TASK_STATUS` for file integrity and status management

------------------------------
Function Details
------------------------------

- `add_task(file_path, todolist_id)` : Prompts the user to enter multiple tasks with title, description, deadline, and status. Saves all tasks to the CSV file.
- `null_todolist_creator(file_path)` : Creates an empty CSV file with headers
- `delete_task(file_path, task_title)` : Marks tasks as deleted and overwrites the CSV file
- `Edit_Task(file_path, task_title)` : Finds a task by title, allows editing of its title, description, deadline, and status
- `Show_the_task(file_path, task_title)` : Displays task details in a readable format

------------------------------
Notes
------------------------------

- Task IDs are generated uniquely per ToDoList
- Deadlines must follow `YYYY/MM/DD` format
- Editing or deleting requires the file to exist
- The module handles input validation to prevent incorrect task information


ماژول وظایف
=============

این ماژول مسئول مدیریت **تسک‌ها** در داخل لیست‌های کار (ToDo Lists) است.

شامل توابعی برای:
    - اضافه کردن تسک‌های جدید
    - ایجاد فایل‌های ToDoList خالی
    - ویرایش و حذف تسک‌ها
    - نمایش تسک‌ها با جزئیات

این ماژول با `storage` برای عملیات CSV و `utils` برای توابع کمکی مانند تولید شناسه، ایجاد ددلاین و دریافت کاربر تعامل دارد.

------------------------------
امکانات اصلی
------------------------------

1. ایجاد تسک
   - `add_task(file_path, todolist_id)` : اضافه کردن تسک به فایل ToDoList
   - `null_todolist_creator(file_path)` : ایجاد فایل ToDoList خالی

2. عملیات تسک
   - `delete_task(file_path, task_title)` : تغییر وضعیت تسک به حذف‌شده در فایل CSV
   - `Edit_Task(file_path, task_title)` : ویرایش ویژگی‌های یک تسک و بروزرسانی فایل
   - `Show_the_task(file_path, task_title)` : نمایش اطلاعات کامل یک تسک

3. ابزارهای کمکی
   - استفاده از `utils.ID_Generator` برای تولید شناسه یکتا
   - استفاده از `utils.Deadline_Creator` برای دریافت ددلاین
   - استفاده از `utils.Editor` و `utils.Get_User` برای ثبت کاربر ایجادکننده یا ویرایشگر
   - کار با ثابت‌هایی مانند `FIELDS_TASKS`، `FILE_STATUS` و `TASK_STATUS` برای مدیریت وضعیت و یکپارچگی فایل

------------------------------
جزئیات توابع
------------------------------

- `add_task(file_path, todolist_id)` : از کاربر می‌خواهد چند تسک با عنوان، توضیحات، ددلاین و وضعیت وارد کند و همه را در فایل CSV ذخیره می‌کند
- `null_todolist_creator(file_path)` : ایجاد فایل CSV خالی با سرفصل‌ها
- `delete_task(file_path, task_title)` : تغییر وضعیت تسک به حذف‌شده و بازنویسی فایل CSV
- `Edit_Task(file_path, task_title)` : پیدا کردن تسک با عنوان، ویرایش عنوان، توضیح، ددلاین و وضعیت آن
- `Show_the_task(file_path, task_title)` : نمایش جزئیات تسک به صورت خوانا

------------------------------
نکات و توصیه‌ها
------------------------------

- شناسه‌های تسک برای هر ToDoList یکتا هستند
- ددلاین‌ها باید با فرمت `YYYY/MM/DD` باشند
- برای ویرایش یا حذف فایل باید وجود داشته باشد
- ماژول شامل اعتبارسنجی ورودی برای جلوگیری از اطلاعات نادرست تسک‌ها است
"""


from datetime import datetime
from config import FIELDS_TASKS,FILE_STATUS,TASK_STATUS,WARNING_COLOR,RESET_COLOR,ATTENTION_COLOR,CORRECT_COLORE
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
            "Task_Status" : TASK_STATUS[1],
            "Create_at" : datetime.today().date(),
            "Edited_by" : utils.Editor(),
            "Create_by" : utils.Get_User(),
            "File_status" :FILE_STATUS[0]
        }
        tasks.append(task)
    storage.write_csv(file_path,FIELDS_TASKS,tasks)
    print(f"task(s) saved in {file_path} successfully")
    
def null_todolist_creator(file_path):
    
    storage.totalwrite_csv(file_path,FIELDS_TASKS)

#endregion

#region : operation function of task :

# ----- delete 
def delete_task(file_path,task_title ) :
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
    if task_title is None:
        task_title = []
        
    if not os.path.exists(file_path):
        print(f"{file_path} does not exist.")
        return
    else:
        tasks = storage.read_csv(file_path)
        task_found = False
        data = []
        deleted_tasks = []
        task_notfound = []
        
        for task in tasks :
    
            if task['Title'].strip().lower() in [t.strip().lower() for t in task_title]:
                deleted_tasks.append(task['Title'])
                task_found = True
                
            else:
                data.append(task)

                
        if not task_found :
            print(f"{WARNING_COLOR}{task_title} not found{RESET_COLOR}")
            return
        else:
            print(f"{CORRECT_COLORE}{deleted_tasks} was found")
            
            
        try :
            storage.totalwrite_csv(file_path,FIELDS_TASKS,data)
        except ValueError as error :
            print(f"{ATTENTION_COLOR}The task deletion operation failed while overwriting the file. Error: {error}{RESET_COLOR} \n")

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
                        task['Task_Status'] = TASK_STATUS[int(i)-1]
                    case __ :
                        print("the input is wrong")
                        return
                        
                task['File_status'] = FILE_STATUS[1]
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
    target_task = [row for row in tasks if (row.get("File_status", "").lower() != "Deleted") and (row.get("Title", "").strip().lower() == task_title.strip().lower())]
    for task in target_task:
            print(f"Title: {task.get('Title', '')} |Descreaption: {task.get('Descreaption', '')} | Status: {task.get('Task_Status', '')}DeadLine: {task.get('DeadLine', '')} | Created at: {task.get('Create_at', '')} ")

#endrigion