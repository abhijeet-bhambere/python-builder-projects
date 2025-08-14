# The ToDo App should follow the input>>processing>>output workflow
# The approach of creating a variable for each todo is NOT sustainable for long-term
# Hence we need to create function that will alter behaviour based on the user input
usrinput = input("Enter in smallcase: ")
result = usrinput.upper()
print(result)

# ================Test only==============
# user_input=input("Enter task: ")
# print(f"User entered - {user_input}")
# Use the list since we need a data type to collect the tasks
# todo1=input("Enter todo1: ")
# todo2=input("Enter todo2: ")
# todo_list = [todo1, todo2]
# print(todo_list)
# The approach of creating a variable is NOT sustainable if we keep on adding tasks
# Hence we need to create function that will alter behaviour based on the user input
