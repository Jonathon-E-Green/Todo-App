import FreeSimpleGUI as sg

FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of the to-do items. """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items to a text file. """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

def get_selected(values):
    """Return selected item or None if nothing selected."""
    try:
        return values['todos'][0]
    except IndexError:
        sg.popup_no_titlebar("Please select a To-Do", font=('Helvetica', 16))
        return None

if __name__ == "__main__":
    print(get_todos())