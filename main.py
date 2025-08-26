import functions
import time


now = time.strftime("%A, %b %d, %Y    %I:%M %p")
print("Today is", now)

while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip().lower()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith("show"):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            row = f"{index + 1}. {item.title().strip('\n')}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter new todo: ") +"\n"
            todos[number] = new_todo

            functions.write_todos(todos)
        except ValueError:
            print("Invalid input")
            continue

    elif user_action.startswith("complete"):
        number = int(user_action[9:])
        try:
            todos = functions.get_todos()
            todo_to_remove = todos[number - 1]
            todos.pop(number - 1)

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove.title().strip('\n')} removed successfully."
            print(message)
        except IndexError:
            print("Enter a valid number")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Invalid input. Try again.")

print("Bye!")