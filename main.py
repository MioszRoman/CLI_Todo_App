import time, os
from functions import get_todos, write_todos

now = time.strftime("%B %d, %Y %H:%M:%S")
print("Today is: ", now)
print("Hello! Welcome to my ToDo App!")
print("1. Show Todo lists\n2. Add new task\n3. Edit task\n4. Complete task\n5. Exit")

user_choice = ""

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

while True:
    user_choice = input("What do you wanna do: ").capitalize()
    user_choice = user_choice.strip()
    if user_choice.startswith("Add"):
        task = user_choice[4:]
        todos = get_todos()
        todos.append(task.capitalize() + '\n')
        write_todos(todos)
    elif user_choice == "Show":
        todos = get_todos()
        for index, task in enumerate(todos):
            task = task.strip('\n')
            print(f"{index+1}: {task}")
    elif user_choice.startswith("Edit"):
        try:
            number = int(user_choice[5:])
            todos = get_todos()
            new_task = input("Enter the edit task: ")
            todos[number-1] = new_task.capitalize() + '\n'
            write_todos(todos)
        except IndexError:
            print("You probably give a number out of list")
        except ValueError:
            print("Probably you forget to add number of task you wanna edit.")
    elif user_choice.startswith("Complete"):
        try:
            number = int(user_choice[9:])
            todos = get_todos()
            print(f"The task {todos[number-1]} was completed!")
            todos.pop(number-1)
            write_todos(todos)
        except IndexError:
            print("Your index is out of the range.")
    elif "Exit" in user_choice:
        print("Bye")
        break
    else:
        print("You write an unknown command.")
