# The ToDo App should follow the input>>processing>>output workflow
# Create such  that takes user input repeatedly (unless interrupted by user): also storing the ToDos in a list 
todo_list = []
edit_flag=False
# Run until user opts to Exit:
while True:
    len_todo = len(todo_list)
    user_action = input(">>>Type add/ edit/ show/ done/ exit: ")
    # using match-case for scenarios based on user input:
    match user_action.lower().strip():
        # for case-1 : adding a task
        case 'add':
            todo = input(">>>Enter task: ")
            todo_list.append(todo)
            print(f"===✅New task Added!===\n{todo_list[-1]}\n")
        # for case-2 : showing tasks added so far
        case 'show':
            if len_todo>0:
                # print(f"Following tasks in the ToDo:")
                # Intro message
                if len_todo==1:
                    print(f"Your ToDo has an open task:")
                elif len_todo >1:
                    print(f"Total {len_todo} tasks in ToDo:")
                # Show the ToDo list
                for index, each in enumerate(todo_list):
                    print(f"{(index+1)} - {each}")
                print("\n")
            else: 
                print("🫙No tasks to show, add a few tasks first to edit\n")
        # case-3: user opts to edit a task
        case 'edit':
            # Remain in edit mode until edit flag is reset
            # Edit mode conditions 1 -- If ToDo list is empty, go back to main menu          
            if len_todo==0:
                print("🫙No tasks to edit, add a few tasks first to edit\n")
                continue

            while True:
                print(f">>>Select Task to edit (a no. between 1 - {len_todo}) OR Cancel :")
                # show the ToDo list
                for index, each in enumerate(todo_list):
                    print(f"{(index+1)} - {each}")
                edit_task_no = input(">>>Enter task no. OR type cancel:")
                # Edit mode conditions--2
                if((edit_task_no).lower()=="cancel"):
                    print("=====⛔Cancelling edit mode=====\n")
                    break
                
                # Edit mode conditions--3
                try: 
                    edit_task_no = int(edit_task_no)
                    while edit_task_no in range(1,len_todo+1):
                        if edit_task_no in range(1,len_todo+1):
                            # check if entered task no. is in range of todo_list indexes
                            # Actual index position in list would be n-1
                            todo_list[(edit_task_no - 1)]=input(">>>Add updated task: ")
                            print(f"=====✅Task no.{edit_task_no} updated!!=====\n")
                            break
                            # Task edit done! Exit the editing mode
                         
                        else :
                            edit_task_no = input(f">>>Enter valid task no.(1 - {len_todo}), OR Cancel :")
                            break
                # elif  edit_task_no!= int(edit_task_no) or (edit_task_no).lower()!="cancel":
                except:    
                    print("\nInvalid input. Please enter a number.\n")
                    continue
    
        # for case-3: mark a task as done
        case 'done':
            if len_todo==0:
                print("🫙No tasks to edit, add a few tasks first to edit\n")
                continue
            else:
                done_task_no = input(f">>>Enter Task No.(1-{len_todo}) to mark as Done:")
                try:
                    done_task_no=int(done_task_no)
                    while done_task_no in range(1,len_todo+1):
                        if done_task_no in range(1,len_todo+1):
                            todo_list.pop(done_task_no-1)
                            print("=====✅Task marked Done!=====\n")
                            break
                        else:
                            print(f">>>No. out of range. Enter Task No.(1-{len_todo})")
                            continue
                except ValueError:
                    print(">>>Invalid value. Enter Task No.(1-{len_todo}) to mark as Done:")
                    continue
        # for case-4: user opts to Exit
        case 'exit':
            break
print("---------end of loop, bye!🔚--------\n")
