import functions
import FreeSimpleGUI as sg
import time

sg.theme('Dark')

# --- Window Layout ---
clock = sg.Text("", key="clock", font=('Helvetica', 12))
label = sg.Text("Type a New To-Do or Select a To-Do to Edit or Complete", key="label")
input_box = sg.InputText(
    tooltip="Enter to-do",
    key="todo",
    size=(46, 10),
    do_not_clear=True  # keep text while typing
)
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
list_box = sg.Listbox(
    values=functions.get_todos(),
    key="todos",
    enable_events=True,
    size=(60, 10)
)

layout = [
    [clock],
    [label],
    [input_box, add_button, edit_button],
    [list_box],
    [complete_button, exit_button],
]

window = sg.Window(
    'My To-Do App',
    layout,
    font=('Helvetica', 16),
    element_justification='c'
)

# Load todos in memory
todos = functions.get_todos()

# --- Event Loop ---
while True:
    event, values = window.read(timeout=1000)

    # Exit cleanly
    if event in (sg.WIN_CLOSED, "Exit"):
        break

    # Update clock on timeout
    if event == sg.TIMEOUT_EVENT:
        window['clock'].update(time.strftime("%A, %b %d, %Y    %I:%M %p"))
        continue  # skip match/case for TIMEOUT_EVENT

    match event:
        case "Add":
            new_todo = values['todo'].strip()
            if not new_todo:
                sg.popup_no_titlebar("Please Add a To-Do", font=('Helvetica', 16))
            elif new_todo in todos:
                sg.popup_no_titlebar("That To-Do already exists!", font=('Helvetica', 16))
            else:
                todos.append(new_todo)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            window['todo'].update("")  # clear input
            window['label'].update(value="Type a New To-Do or Select a To-Do to Edit or Complete")

        case "Edit":
            todo_to_edit = functions.get_selected(values)
            if todo_to_edit:
                new_todo = values['todo'].strip()
                if new_todo:
                    index = todos.index(todo_to_edit)
                    todos[index] = new_todo
                    functions.write_todos(todos)
                    window['todos'].update(values=todos)
                    window['todo'].update("")
                    window['label'].update(value="Type a New To-Do or Select a To-Do to Edit or Complete")

        case "Complete":
            todo_to_complete = functions.get_selected(values)
            if todo_to_complete:
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update("")
                window['label'].update(value="Type a New To-Do or Select a To-Do to Edit or Complete")
                sg.popup_no_titlebar(f"{todo_to_complete} Has Been Completed", font=('Helvetica', 16))

        case "todos":
            todo_selected = functions.get_selected(values)
            if todo_selected:
                window['todo'].update(todo_selected)
                window['label'].update(value=f"Edit or complete: {todo_selected}")

window.close()