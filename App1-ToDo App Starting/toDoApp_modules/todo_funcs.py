# **********************************New Functions***********************************
"""Module for the toDoApp main py file.

Contains the `get_todos` and `write_todos` funcs"""
# get_todo func--reads txt & displays the ToDos
def get_todos(txtfile_path):
    """reads txt file & displays the ToDos as a list"""
    with open(txtfile_path,"r") as f:
        contents = f.readlines()
        todo_list_int = [x.strip("\n") for x in contents]
    return todo_list_int

# write_todo function is more like a procedure - not meant to return any value
def write_todos(txtfile_path,todo_list):
    """This func is more like a procedure - not meant to return any value.

    Writes the updated `todo_list` back into the txt file."""
    with open(txtfile_path,"w") as f:
        f.writelines([x + "\n" for x in todo_list])
