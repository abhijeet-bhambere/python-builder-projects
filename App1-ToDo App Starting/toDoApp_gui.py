import todo_functions as tf
import FreeSimpleGUI as sg
import time
# Setting an app theme 
sg.theme('BrownBlue')
# Defining a window instances using .Window class
# Defining arguments to be passed in the window object
# NEW-- added datetime  
label_clock = sg.Text('',key="clock") 
label = sg.Text("Type a ToDo")
inputbox = sg.InputText(tooltip="Enter a ToDo:", key="todo")
addbutton = sg.Button("Add")
editbutton = sg.Button("Edit")
donebutton = sg.Button("Done")
exitbutton = sg.Button("Exit App")

# displaying the existing ToDos:
list_box = sg.Listbox(values=tf.get_todos(), key="todos", enable_events=True, size=[50,18])

# Set the layout in the app's window 
layout = [[label_clock],
        [label], 
        [inputbox,addbutton],
        [list_box, editbutton, donebutton],
        [exitbutton]]
# With a multi-line window layout
window = sg.Window("The ToDo App", font=('Helvetica',10) ,layout=layout)

# Adding user actions under a while loop-- similar to main py file code
while True:
    # Displays the window -- capture resulting tuple in differnt variables 
    # Event captures what user action was taken ; Values captures the actual user inputs
    event,values = window.read(timeout=300)
    print(event)
    print(values)
    # Added datetime display
    window['clock'].Update(value=time.strftime("%b-%d-%Y, %H:%M"))

    match event:
        case"Add":
            # Fetch todos list from the txt file
            todo_list = tf.get_todos()
            # Add the new todo key value once user clicks on Add button
            todo_list.append(values['todo'])
            tf.write_todos(todo_list)
            # Update listBox element
            window["todos"].Update(values=todo_list)
        case "Edit":
            try:
                # Fetching value of the selected ToDo from listBox (event's value )
                # This is the existing ToDo
                existing_todo = values["todos"][0]
                # The NEW ToDo for that task no.
                updated_todo = values['todo']
                # Calling the existing list
                todo_list = tf.get_todos()
                # Fetching index no. of the selected ToDos from listBox 
                task_number = todo_list.index(existing_todo)
                # Replacing with the new ToDo in the list
                todo_list[task_number] = updated_todo
                # Updating txt file with new ToDo
                tf.write_todos(todo_list)
                # Access updated listBox to refresh & display updated ToDo list in real-time
                window['todos'].Update(values=todo_list)
            except IndexError:
                sg.popup("Select a ToDo first...", font=('Helvetica',10))


        case "Done":
            try:
                # Selected Task by user on App (from listBox)
                todo_done = values['todos'][0]
                # Fetch the actual todo_list
                todo_list = tf.get_todos()
                # Mark done i.e. Remove the selected todo from the todo_list
                todo_list.remove(todo_done)
                # Update the todoList in txt file
                tf.write_todos(todo_list=todo_list)
                # Access updated listBox to refresh & display updated ToDo list in real-time
                window['todos'].Update(values=todo_list)
                # Also update the inputBox value on ExitButton action
                window['todo'].Update(values='')
            except IndexError:
                sg.popup("Select a ToDo first...", font=('Helvetica',10))

        case "Exit App":
            break

        case 'todos':    
            # Added functionality to 
            window["todo"].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break

window.close()


