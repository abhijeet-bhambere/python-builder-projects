from toDoApp_modules import todo_funcs
import FreeSimpleGUI as sg

# Setting an app theme 
sg.theme('dark blue 14')
# Defining a window instances using .Window class
# Defining arguments to be passed in the window object
label = sg.Text("Type a ToDo")
inputbox = sg.InputText(tooltip="Enter a ToDo:", key="todo")
addbutton = sg.Button("Add")

# # With a simple window layout
# window = fsg.Window("The ToDo App", layout=[[label, inputbox]])

# With a multi-line window layout
window = sg.Window("The ToDo App", 
                   layout=[[label], [inputbox,addbutton]], 
                   font=('Roboto',14)
                   )

# Displays the window -- capture resulting tuple in differnt variables 
# Event captures what user action was taken ; Values captures the actual user inputs
event,values = window.read()
print(event)
print(values)

window.close()


