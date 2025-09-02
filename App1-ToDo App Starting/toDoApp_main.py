# The ToDo App should follow the input>>processing>>output workflow
# Create such  that takes user input repeatedly (unless interrupted by user): also storing the ToDos in a txt file
import os
# todo_list = [] #***Earlier starting point to initialize empty list***
# ***********************New Starting point -- read/write to a txt file*************************

# Create file in the same path as py file
pyfile_path = os.path.dirname(os.path.abspath(__file__))
txtfile_path = os.path.join(pyfile_path,"todoList.txt")
# Check if file already exists -- else create new file
if os.path.exists(txtfile_path):
    with open(txtfile_path,"r") as f:
        # Replicates same todo_list=[] as earlier method ; also removes \n character 
        # If its empty file, then empty list is created anyways
        contents = f.readlines()
        todo_list = [x.strip("\n") for x in contents]
    # Else create & open an empty file & also initiate an empty list
else:
    with open(txtfile_path,"w") as f:
        # List used for operations -- add, show, edit, done
        todo_list=[]

# *****************************Run until user opts to Exit:****************************************
while True:
    len_todo = len(todo_list)
    # *********************************Main action selection********************************
    user_action = input(">>>Type add/ edit/ show/ done/ exit: ")
    user_action = user_action.lower().strip()
    # moving to if-else for scenarios based on user input:
        # ***************for case-1 : adding a task*****************************************
    if 'add' in user_action:
        todo = user_action[4:]
        todo_list.append(todo)
        # Add single task to the end of existing file
        with open(txtfile_path,"a") as f:
            f.write(todo + "\n")
        print(f"===✅New task Added!===\n{todo_list[-1]}\n")
    # ********************for case-2 : SHOW added tasks*************************************
    elif 'show' in user_action:
        if len_todo>0:
            # print(f"Following tasks in the ToDo:")
            # Intro message
            if len_todo==1:
                print(f"====📄Your ToDo has an open task:====")
            elif len_todo >1:
                print(f"====📄Your ToDo has {len_todo} Open tasks:====")
            # Show the ToDo list
            with open(txtfile_path,"r") as f:
                inter=[x.strip() for x in f.readlines()]
                for index,val in enumerate(inter):
                    print(f"{index+1}-{val}")
            
            #for index, each in enumerate(todo_list):
            #    print(f"{(index+1)} - {each}")
            print("\n")
        else: 
            print("🫙No tasks to show, add a few tasks first to edit\n")
    # *********************case-3 : user opts to edit a task*********************************
    # Creating much simplified Edit mode--user directly mentions task to edit in options itself
    elif 'edit' in user_action:
        # Remain in edit mode until edit flag is reset
        # Edit mode conditions 1 -- If ToDo list is empty, go back to main menu          
        if len_todo==0:
            print("🫙No tasks to edit, add a few tasks first to edit\n")
            continue
        else:
            edit_task_no = int(user_action[4:])
        # while True:
        #     print(f">>>Select Task to edit (a no. between 1 - {len_todo}) OR Cancel :")
        #     # show the ToDo list
        #     with open(txtfile_path,"r") as f:
        #         inter=[x.strip() for x in f.readlines()]
        #         for index,val in enumerate(inter):
        #             print(f"{index+1}-{val}")
        #     # Ask for user choice
        #     edit_task_no = input(">>>Enter task no. OR type cancel:")
        #     # Edit mode conditions--2
        #     if((edit_task_no).lower()=="cancel"):
        #         print("=====⛔Cancelling edit mode=====\n")
        #         break
            
            # Edit mode conditions--3

            try:
                if edit_task_no in range(1,len_todo+1):
                    # check if entered task no. is in range of todo_list indexes
                    # Actual index position in list would be n-1
                    todo_list[(edit_task_no - 1)]=input(">>>Add updated task: ")
                    # Modify the task & add entire list to txt                           
                    with open(txtfile_path,"w") as f:
                        f.writelines([x + "\n" for x in todo_list])
                    print(f"=====✅Task no.{edit_task_no} updated!!=====\n")
                    
                    # Task edit done! Exit the editing mode
                    
                else :
                    print(f"⚠️  Enter valid task no.(1 - {len_todo}) to edit")
                    
            # elif  edit_task_no!= int(edit_task_no) or (edit_task_no).lower()!="cancel":
            except:    
                print("\nInvalid input. Please enter a number.\n")
                

    # ************************for case-4: mark a task as done*********************************
    # Adding similar logic to reduce user input actions to mark a ToDo as 'done'
    elif 'done' in user_action:
        if len_todo==0:
            print("🫙No tasks to edit, add a few tasks first to edit\n")
            # continue
        
        else:
            try:
                # Ask user input - directly taken from main action selection step
                # done_task_no = input(f">>>Enter Task No.(1-{len_todo}) to mark as Done:")
                done_task_no = int(user_action[5:])

                if done_task_no not in range(1,len_todo+1):
                    print(f"⚠️ Enter valid Task No. between (1-{len_todo})")
            
                elif done_task_no in range(1,len_todo):                
                    # while done_task_no in range(1,len_todo+1):
                    todo_list.pop(done_task_no - 1)

                        # Remove the task & add updated list to txt file
                    with open(txtfile_path,"w") as f:
                        f.writelines([x+"\n" for x in todo_list])
                    print("=====✅  Task marked Done!=====\n")
                
                else:
                    print(f">>>No. out of range. Enter Task No.(1-{len_todo+1})")
                        
            except ValueError:
                print(f"⚠️ Enter valid Task No. between (1-{len_todo}) to mark as Done:")
                    
    # ******************************for case-5: user opts to Exit*****************************
    elif 'exit' in user_action:
        break
    else:
        print("Enter valid command from the options")
print("---------end of loop, bye!👋🏻--------\n")
