import argparse
import tasks
import utils
import sys

if __name__ == "__main__":
    raise RuntimeError("Run the main program (main.py), not cli.py directly")


#description of commands
desc_prog = "This program creat the To Do List to JSON format"
desc_add_task = "Use this command to creat a task, by writing the name of task"
desc_update = "Use this command to change the name of the task"
desc_delete = "Use this command to delete the task"
desc_mark = "Use this command to change the status of the task"
desc_list = "Use this command to list all tasks"
#region : the parser and argument definition

#main structure
parser = argparse.ArgumentParser(description=desc_prog)
subparser = parser.add_subparsers(dest= "command")

#add_task
add_parser = subparser.add_parser("add",description=desc_add_task , help="add a new task")
add_parser.add_argument("task_name",type=str,help = "name of task")

#update_task
update_parser = subparser.add_parser("update", help = "update the task",description=desc_update)
update_parser.add_argument("task_id",type=int,help="the task index that you wana update it")
update_parser.add_argument("new_name",type=str,help="new name of task")

#delete_task
delete_parser = subparser.add_parser("delete",description=desc_delete,help="delete the task by input index")
delete_parser.add_argument("task_id",type=int,help="the task index that be deleted")

#mark
mark_parser = subparser.add_parser("mark",description=desc_mark)
mark_parser.add_argument("task_index",type=int,help = "the task index that changing")
mark_parser.add_argument("--in_progress",action= "store_true",help = "Mark as in progress")
mark_parser.add_argument("--done",action="store_true",help="Mark as done")

# list
list_parser =  subparser.add_parser("list",description=desc_list)
list_parser.add_argument("--task_status", type=str,help= "status the tasks that you want to list it")


#region : help description

def show_help():
    print("""
          add tasks : add <name of task>
          update  
          """)

#endregion

#region : call the function
def main():
     
            args = parser.parse_args(sys.argv[1:])
            if args.command == "add":
                tasks.add_task(args.task_name)
            elif args.command == "update":
                task = utils.find_task_by_id(args.task_id)
                tasks.update_task(task,description = args.new_name,statue = task["Status"])
        
            elif args.command == "delete": # cheched!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                tasks.delete_task(args.task_id)
        
            elif args.command == "mark":
                tasks.mark(args.task_id,in_progress=args.in_progress,done = args.done)
            elif args.command == "list":
                print (utils.creat_list(args.task_status))
            else :
                show_help()
 

