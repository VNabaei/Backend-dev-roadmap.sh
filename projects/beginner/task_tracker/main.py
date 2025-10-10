import sys
from pathlib import Path

# اضافه کردن مسیر moduls به sys.path
sys.path.append(str(Path(__file__).parent / "moduls"))

from moduls import cli
from moduls import config
from moduls import storage


# چون نشد آدرس هارو در ماژول اوکی کنم فعالا آدرس دهی مستقیم است
# RUN_FILE_PATH, RUN_DIR, DATA_DIR, TASKS_FILE = config.init_paths()

# storage.init_storage(TASKS_FILE)


#FIXIT:dir of data is incorrect!



def main():
    print("""
          welcome to task tracker\n
          created by vaghar nabaei ver: 1.0.0\n
          START:\n 
          for creat a task please type :  add <name or description>\n
          for update a task type : update <id of task> <change the name or description>\n
          for delete a task type : delete <id of task>\n
          note : for update or delete, first list all the task to visit ids\n
          for show list :\n
          list all tasks : write "list"\n
          list todo tasks : write "list" --todo\n
          list done tasks : write "list" --done\n
          list in progress tasks : write "list" --in_progress\n
          enjoy :))\n
          """)   
    cli.main()



if __name__ == "__main__" :
    main()
    
    
#خطا ها:
""" این برنامه در bash درست اجرا نمیشود.
cli نمیتواند دستورات ورودی را درست تفکیک کند
دستور add first  اجرا نمی شود.
در آینده  وصعیت کلی تسک هارا اضافه کن در هنگام شروع"""