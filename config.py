import os

#region : Constants and variable 

#path of app : 
BASE_DIR_PATH = os.getcwd()
APP_FOLDER_PATH = os.path.join(BASE_DIR_PATH,"Todolists app")
TABLE_LIST_PATH = os.path.join(APP_FOLDER_PATH,"Table_List.csv")

# filesds in Task and List :
FIELDS_TASKS = ['Id','Title','Descreaption','DeadLine','Task_Status', 'Create_at','Edited_by','File_status'] 
FIELDS_TABLE = ['Id','Title','Creator','Created_at','File_status','Path']

#Status in file status ana task :
FILE_STATUS = ['Created','Edited','Deleted']
TASK_STATUS = ['Done','Todo','In_progress','Deleyed']

# color :
WARNING_COLOR = "\033[91m" 
ATTENTION_COLOR = "\033[93m"
RESET_COLOR = "\033[0m"

#endregion