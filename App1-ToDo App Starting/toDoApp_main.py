# The ToDo App should follow the input>>processing>>output workflow
# Create such  that takes user input repeatedly (unless interrupted by user): also storing the ToDos in a txt file

# *********************************NEW--Defining functions**************************************
# Create file in the same path as py file
# import os
# pyfile_path = os.path.dirname(os.path.abspath(__file__))
# txtfile_path = os.path.join(pyfile_path,"todoList.txt")

# **********New-Functions shifted into same location as main py file***********
import todo_functions as todo_funcs
import time

# Fetch todoList OR create one in a first-runtime scenario
todo_list = todo_funcs.get_todos()


# ***********************************>Run until user opts to Exit:<*******************************
while True:
    len_todo = len(todo_list)
    # *********************************Main action selection********************************
    user_action = input(">>>Type add/ edit/ show/ done/ exit: ")
    user_action = user_action.lower().strip()

    # **************************for case-1 : adding a task*********************************
    if user_action.startswith('add'):
        todo = user_action[4:]
        # Add single task to the end of existing file
        todo_list.append(todo)
        # Invoking the write_todo function
        todo_funcs.write_todos(todo_list=todo_list)
        print(f"===✅New task Added!===\n{todo_list[-1]}\n")

    # **************************for case-2 : SHOW added tasks******************************
    elif user_action.startswith('show'):
        if len_todo>0:
            if len_todo==1:
                print(f"====📄Your ToDo has an open task:====")
            elif len_todo >1:
                print(f"====📄Your ToDo has {len_todo} Open tasks:====")
            # Show the ToDo list
            inter=todo_funcs.get_todos()
            for index,val in enumerate(inter):
                print(f"{index+1}-{val}")
            
            print("\n")
        else: 
            print("🫙No tasks to show, add a few tasks first to edit\n")

    # ************************case-3 : user opts to edit a task*****************************
    # A simplified Edit mode--user directly mentions task No. to edit in options itself
    elif user_action.startswith('edit'):
        # Remain in edit mode until edit flag is reset
        # Edit mode conditions 1 -- If ToDo list is empty, go back to main menu          
        if len_todo==0:
            print("🫙No tasks to edit, add a few tasks first to edit\n")
            continue
        try:
            edit_task_no = int(user_action[4:])            
            # Edit mode conditions--3
            
            if edit_task_no in range(1,len_todo+1):
                # check if entered task no. is in range of todo_list indexes
                # Actual index position in list would be n-1
                todo_list[(edit_task_no - 1)]=input(f">>>Update ToDo no.{edit_task_no} OR cancel update: ").lower().strip()
                if todo_list[(edit_task_no - 1)].startswith("cancel"):
                    print(f"=====🚫 Update cancelled=====")
                    continue
                # Modify the task & add entire list to txt
                else:
                    todo_funcs.write_todos(todo_list=todo_list)
                    print(f"=====✅Task no.{edit_task_no} updated!!=====\n")                
                # Task edit done! Exit the editing mode
                
            else :
                print(f"⚠️  Enter valid task no.(1 - {len_todo}) to edit")
                
        # elif  edit_task_no!= int(edit_task_no) or (edit_task_no).lower()!="cancel":
        except ValueError:    
            print("\n⚠️  Invalid input. Please enter a number.\n")            

    # ************************for case-4: mark a task as done*********************************
    # Adding similar logic to reduce user input actions to mark a ToDo as 'done'
    elif user_action.startswith('done'):
        if len_todo==0:
            print("🫙No tasks to edit, add a few tasks first to edit\n")
        
        else:
            try:
                # Ask user input - directly taken from main action selection step
                done_task_no = int(user_action[5:])

                try:
                    done_task_no = int(user_action[5:])
    
                    # if done_task_no in range(1,len_todo+1):
                    todo_list.pop(done_task_no - 1)

                    # Remove the task & add updated list to txt file
                    todo_funcs.write_todos(todo_list=todo_list)
                    print("=====✅  Task marked Done!=====\n")
                
                except IndexError:
                    print(f"⚠️ Task No. not in range. Enter a valid no. between (1-{len_todo})")
                    continue            
                                        
            except ValueError:
                print(f"⚠️ Enter valid Task No. between (1-{len_todo}) to mark as Done:")
                continue
                    
    # ******************************for case-5: user opts to Exit*****************************
    elif user_action.startswith('exit'):

        break
    
    # ******************************for case-6: invalid user input*****************************
    else:

        print("Enter valid command from the options")

print('===exiting', end='', flush=True)
for _ in range(4):
    time.sleep(0.5)
    print(".", end='',flush=True)
print('===\n', end='', flush=True)
print('===================================================================')
print("|------------------------------THE END----------------------------|")
print('===================================================================')
