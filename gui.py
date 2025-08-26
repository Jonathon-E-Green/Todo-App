import functions
import FreeSimpleGUI as fsg

label = fsg.Text("Type in a to-do")
input_box = fsg.InputText(tooltip="Enter to-do")
add_button = fsg.Button("Add")

window = fsg.Window('My To-Do App', layout=[[label], [input_box, add_button]])
window.read()
window.close()