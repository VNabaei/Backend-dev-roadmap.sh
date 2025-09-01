"""
Config Module
=============

This module contains constants and variables used across the ToDoList application.

It includes definitions for:
    - Application folder paths
    - CSV file paths
    - Field names for tasks and lists
    - Status values for files and tasks
    - ANSI color codes for terminal output

------------------------------
Constants
------------------------------

1. Paths:
   - BASE_DIR_PATH : str : Current working directory
   - APP_FOLDER_PATH : str : Path to store ToDoList application data
   - TABLE_LIST_PATH : str : Path to the main ToDoList table CSV file

2. Fields:
   - FIELDS_TASKS : list : Column headers for task CSV files
   - FIELDS_TABLE : list : Column headers for the main list table

3. Status:
   - FILE_STATUS : list : ["Created", "Edited", "Deleted"]
   - TASK_STATUS : list : ["Done", "Todo", "In_progress", "Deleyed"]

4. Colors:
   - WARNING_COLOR / EXPIRED_COLOR : Red (\033[91m)
   - ATTENTION_COLOR / DUE_TODAY_COLOR : Yellow (\033[93m)
   - RESET_COLOR : Reset (\033[0m)
   - CORRECT_COLOR / ACTIVE_COLOR : Green (\033[92m)


ماژول Config
=============

این ماژول شامل ثابت‌ها و متغیرهایی است که در سرتاسر برنامه ToDoList استفاده می‌شوند.

شامل تعریف‌ها برای:
    - مسیرهای پوشه برنامه
    - مسیر فایل‌های CSV
    - نام ستون‌های فایل‌های تسک و جدول لیست‌ها
    - مقادیر وضعیت فایل و تسک‌ها
    - کدهای رنگ ANSI برای خروجی ترمینال

------------------------------
ثابت‌ها
------------------------------

1. مسیرها:
   - BASE_DIR_PATH : str : مسیر جاری (Current working directory)
   - APP_FOLDER_PATH : str : مسیر ذخیره داده‌های برنامه ToDoList
   - TABLE_LIST_PATH : str : مسیر فایل CSV جدول اصلی لیست‌ها

2. ستون‌ها:
   - FIELDS_TASKS : list : نام ستون‌های فایل CSV تسک‌ها
   - FIELDS_TABLE : list : نام ستون‌های جدول اصلی لیست‌ها

3. وضعیت:
   - FILE_STATUS : list : ["Created", "Edited", "Deleted"]
   - TASK_STATUS : list : ["Done", "Todo", "In_progress", "Deleyed"]

4. رنگ‌ها:
   - WARNING_COLOR / EXPIRED_COLOR : قرمز (\033[91m)
   - ATTENTION_COLOR / DUE_TODAY_COLOR : زرد (\033[93m)
   - RESET_COLOR : ریست (\033[0m)
   - CORRECT_COLOR / ACTIVE_COLOR : سبز (\033[92m)


"""

import os

#region : Constants and variable 

#path of app : 
BASE_DIR_PATH = os.getcwd()
APP_FOLDER_PATH = os.path.join(os.path.join(BASE_DIR_PATH,"data"),"ToDoList_App")

TABLE_LIST_PATH = os.path.join(APP_FOLDER_PATH,"Table_List.csv")

# filesds in Task and List :
FIELDS_TASKS = ['Id','Title','Descreaption','DeadLine','Task_Status', 'Create_at','Create_by','Edited_by','File_status'] 
FIELDS_TABLE = ['Id','Title','Creator','Created_at','File_status','Path']

#Status in file status ana task :
FILE_STATUS = ['Created','Edited','Deleted']
TASK_STATUS = ['Done','Todo','In_progress','Deleyed']

# color :
WARNING_COLOR = EXPIRED_COLORE = "\033[91m" 
ATTENTION_COLOR = DUE_TODAY_COLOER = "\033[93m"
RESET_COLOR = "\033[0m"
CORRECT_COLORE =ACTIVE_COLORE ="\033[92m"

#endregion