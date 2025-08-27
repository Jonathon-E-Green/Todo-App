import functions
import FreeSimpleGUI as sg
import time

sg.theme('Dark')

date = time.strftime("%A, %b %d, %Y")
clock = sg.Text(date, font=('Helvetica', 12))
label = sg.Text("Type a New To-Do or Select a To-Do to Edit or Complete", key="label")
input_box = sg.InputText(tooltip="Enter to-do", key="todo", size=(46, 10),
                         do_not_clear=False, default_text="")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                       enable_events=True, size=(60, 10))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window('My To-Do App',
                    layout=[[clock],
                            [label],
                            [input_box, add_button, edit_button],
                            [list_box],
                            [complete_button, exit_button]],
                    font=('Helvetica', 16),
                    element_justification='c')

while True:
    event, values = window.read()

    match event:
        case "Add":
            if not values['todo'].strip():
                sg.popup_no_titlebar("Please Add a To-Do", font=('Helvetica', 16))
            else:
                todos = functions.get_todos()
                new_todo = values['todo'] + "\n"
                todos.append(new_todo.title())
                functions.write_todos(todos)
                window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + "\n"

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo.title()
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['label'].update(value="Type a New To-Do or Select a\nTo-Do to Edit or Complete")
            except IndexError:
                sg.popup_no_titlebar("Please select a To-Do", font=('Helvetica', 16))
        case "Complete":
            try:
                todos = functions.get_todos()
                complete_todo = values['todos'][0]
                complete_to_display = complete_todo.strip('\n')
                index = todos.index(complete_todo)
                todos.pop(index)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['label'].update(value="Type a New To-Do or Select a\nTo-Do to Edit or Complete")
                sg.popup_no_titlebar(f"{complete_to_display} Has Been Completed", font=('Helvetica', 16))
            except IndexError:
                sg.popup_no_titlebar("Please select a To-Do", font=('Helvetica', 16))
        case "todos":
            try:
                selected_todo = values['todos'][0]
                window['todo'].update(selected_todo.strip('\n'))
                window['label'].update(value=f"Edit or complete: {selected_todo}")
            except IndexError:
                continue
        case "Exit":
            break

        case sg.WIN_CLOSED:
            exit()

window.close()