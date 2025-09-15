
from modules import storage,lists,tasks,utils

from config import WARNING_COLOR,ATTENTION_COLOR,RESET_COLOR,TABLE_LIST_PATH,CORRECT_COLORE


#region : operation function:

def Show2Select():
        '''
        To show list Titles while adding or editing tasks
        
        Parametr(s):
        -----------
        None
        
        Return(s):
        ---------
        path_of_list :str
            String containing the path value of the desired list. 
        '''
        print("select the title of the lists : \n")
        lists.show_All_lists()
        Target_list = input("+input the title: \n")
        try :
            path_of_list = utils.getPath(Target_list)
            lists.Show_List(path_of_list)
            
            print("all task(s) :\n")
            lists.Show_List_ALLTask(path_of_list)
            return path_of_list
        except Exception as error:
            print(f"{WARNING_COLOR} Error : list not found.\n detail:({error}){RESET_COLOR}")
            return None

#endregion

#region : menu
#----------------------------------------------------------------------------------

#region : inner menu                     
def edit_menu():
    '''
    This function is used in the internal menu section to edit tasks and lists such as updating, deleting, and adding tasks.
    
    Parametr(s):
    -----------
    None
    
    Return(s):
    ---------
    None
    '''
    if not utils.check_lists_exists() :
        print(f"{ATTENTION_COLOR}Please create a todo list first.{RESET_COLOR}")
        return
    while True:
        print("\nEditing .........................................\n")
        print("1.Add a new task\n2.Edit a task \n3.Delete a task \n4.View all tasks"
              "\n5.Delete List \n7.Back to main menu \n8.Exit")
        edit_choice = input("+Enter your choice: ")
        
        if edit_choice == "1":
            print("----\nadd task(s) -------------------------\n ")
            print("for adding, do this steps :\n")
            lists.show_All_lists()
            
            Target_list= input("+Which list do you want to add task(s)? ")
            # try :
            todo_list_path = utils.getPath(Target_list)  
            tasks.add_task(todo_list_path ,utils.getId(Target_list))
            # except Exception :
                # print(f"{ATTENTION_COLOR}Something is wrong with the input variable. Erorr :{RESET_COLOR}")
            
        elif edit_choice == "2":
            print("----\nEdit a task -------------------------\n ")
            print("for edit, do this steps :\n")
            path_of_list = Show2Select()
            if path_of_list :
                ETask = input("+Enter the Title of the task to edit: ")
                try :
                    
                    tasks.Edit_Task(path_of_list,ETask)
                except Exception :
                    print(f"{ATTENTION_COLOR}Something is wrong with the input variable. Erorr :{RESET_COLOR}")
                    
                # if the task is found, you would update it here

                
        elif edit_choice == "3":
            print("----\nDelete a task -------------------------\n ")
            print("for delete, do this steps :\n")
            path_of_list = Show2Select()
            if path_of_list :
                deleteTask = input("+Enter the Title(s) of the task(s) to delete: [Use commas(,) to separate titles.] ").split(",")
                try :
                    tasks.delete_task(path_of_list,deleteTask)
                    print(f"{CORRECT_COLORE}The process was completed successfully.{RESET_COLOR}")
                except Exception :
                    print(f"{ATTENTION_COLOR}Something is wrong with the input variable. Erorr :{RESET_COLOR}")
                 
            
        elif edit_choice == "4":
            print("----\nView all tasks in list ----------------\n ")
            print("select the title of the lists : \n")
            lists.show_All_lists()
            
            Target_list = input("+input the title: \n")
            try :
                
                path_of_list = utils.getPath(Target_list)
                lists.Show_List(path_of_list)
            except Exception :
                print(f"{ATTENTION_COLOR}Something is wrong with the input variable.{RESET_COLOR}")
                 

        elif edit_choice == "5":
            print("----\nDelete a list -------------------------\n ")

            lists.show_All_lists()
            print("select the title of the lists : \n")
            try :
                Target_list = input("+input the title: \n")
                path_of_list = utils.getPath(Target_list)
                confirm_delete = input("+Do you want to delete it completely? (y/n) ")

                if  confirm_delete.lower().strip() == 'y':
                    lists.delete_List(path_of_list,TABLE_LIST_PATH) 
                    print("List deleted successfully")  
                else:
                    print(f"{ATTENTION_COLOR}the process canceled{RESET_COLOR}")
            except Exception :
                print(f"{ATTENTION_COLOR}Something is wrong with the input variable. Erorr :{RESET_COLOR}")
                 
            
        # elif edit_choice == "6":
        #     print("----\nUpdate the List -----------------------\n ")
        #     #TODO : implement update feature later
            
        elif edit_choice == "7":
            print("\nmain menu -----------------------------\n ")
            break
        elif edit_choice == "8":
            print("----\nexiting -------------------------------\n ")
            print("(T_T)\n ")
            exit()
            
        else:
            print(f"{ATTENTION_COLOR}wrong input please try again later :)\n")
            print(f"Returning to the main menu{RESET_COLOR}")
            print("------------------------------------------------")
            break
#endregion            

#region :  main menu       

def main_menu():
    '''
    The main menu of the program, which contains the list, add list, and edit list.
    
    Parametr(s):
    -----------
    None
    
    Return(s):
    ----------
    None
    '''
    #operation :
    
    print(f"---------------- To Do List(s) in this Application ----------------\n")
    try : 
        utils.chack_the_lists_in_table_list()
        lists.show_All_lists()
    except ValueError as a: 
        print (f"error in showing the list {a}")
    while True:

        print ("\nMenu :")
        print ("1.Create a new List\n2.Edit a List\n3.show the tasks \n4.Exit")
        main_choice = input("+Enter your choice: ")
        
        if main_choice == "1":
            print("\nCreating new list ...............................\n ")
            #---- input the input_Title of the list
            List_Title = input("+Enter the Title of the list: ")          
            #---- create a new list
            #---- add the list to the file
            if not List_Title == "" :
                path = lists.Create_New_list(List_Title)
            #---- for add tasks this is run in the function Create_New_list
            #---- if the user want to add tasks, this function will be called
            else :
                print(f"{ATTENTION_COLOR}Unknow input .-.-.-.-.-.-.-.-.-.-.-.-.-..-.--.-.-.-.-.-\n ")

                print(f"wrong input please try again :){RESET_COLOR}")
                continue
                
        elif main_choice == "2":
            edit_menu()
            
        elif main_choice == "3":
            print("\nShowing : .................................\n ")
            if lists.show_All_lists() :
                try :
                    Target_list= input("+what list do you want to show?\n:")
                    todo_list_path = utils.getPath(Target_list)    
                    lists.Show_List(todo_list_path)
                except Exception :
                    print(f"{WARNING_COLOR}Something is wrong with the input variable.{RESET_COLOR}")
                    
            else :
                print(f"{ATTENTION_COLOR}please create a todo list first.{RESET_COLOR}")
                continue
                    
            
            
        elif main_choice == "4":
            print("\nExiting from prograss .....................\n ")

            print("Khosh Galdin")
            break
        
        else :
            print(f"{ATTENTION_COLOR}Unknow input .-.-.-.-.-.-.-.-.-.-.-.-.-..-.--.-.-.-.-.-\n ")

            print(f"wrong input please try again :){RESET_COLOR}")

#endregion        

#endregion            
                        
#region :   ---------- run the program 
print("\nwelcome to the ToDolist app\n")

if __name__ == "__main__":

    main_menu()
        
#endregion        