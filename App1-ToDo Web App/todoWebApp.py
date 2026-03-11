# Core idea of this app is to leverage session state's callback capability\n
# To make use of the key-value pairs to get the  
import streamlit as st
import todo_functions as tf

# Adding the title and subtitle
st.title("The ToDo App")
st.write("A web version of the terminal-based Task manager app")
# dummy checkpoint
# st.checkbox("dummyTask1")

# getting the list (or creating at first-run scenario)
todos = tf.get_todos()
st.write(f"You've got {len(todos)} open tasks")

# display the updated ToDo list
# rev2 - Added logic for 'task Done' case ; st.rerun resets execution flow
for i,todo in enumerate(todos):
    checkbox_var = st.checkbox(todo,key=todo)
    # remove the task if its checked
    if checkbox_var:  
        todos.pop(i)
        # Update todolist txt
        tf.write_todos(todos)

        del st.session_state[todo]
        #restarts the py script from beginning
        st.rerun() 

# rev2: adding function to get session state
# Enables callback to previous state and write to ToDo list
def add_newtask():
    newtask = st.session_state["new_task"]
    if newtask:
        # Added input validation: avoids writing empty task 
        todos.append(newtask)
        tf.write_todos(todos)
        st.session_state["new_task"]=''

st.divider()
# Getting user input (new task)
st.text_input("Enter ToDo", placeholder="Add new todo",
              on_change=add_newtask,key='new_task')# Enables callback to previous state

# checking session state: basically a dictionary that enables sharing
# variables between reruns, for each user session
# Also enables Callbacks - esp. useful in multi-page app
st.session_state

