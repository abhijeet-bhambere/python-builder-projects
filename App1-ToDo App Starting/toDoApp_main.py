# The ToDo App should follow the input>>processing>>output workflow

# Create function that takes user input repeatedly (unless interrupted by user):
# Hence, implementing a while loop with an incrementing variable ; also storing the ToDos in a list 
todo_list = []

n=0

# Run for finite no. of loops -- accept only 3 tasks for now
while n<3:
    user_action = input("Type add / show/ exit: ")
    
    match user_action.lower().strip():
        case 'add':
            todo = input("Enter task: ")
            todo_list.append(todo)
            print(todo_list)
            n+=1

        case 'show':
            print(f"Following tasks in the ToDo: {todo_list}")
            for index, each in enumerate(todo_list):
                print(f"{(index+1)} - {each}")

        case 'exit':
            break
print("---------end of loop, bye!--------")
# ================Day 1 Testing==============
# user_input=input("Enter task: ")
# print(f"User entered - {user_input}")
# Use the list since we need a data type to collect the tasks
# todo1=input("Enter todo1: ")
# todo2=input("Enter todo2: ")
# todo_list = [todo1, todo2]
# print(todo_list)
# The approach of creating a variable is NOT sustainable if we keep on adding tasks
# Hence we need to create function that will alter behaviour based on the user input
