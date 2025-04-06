import time

now = time.strftime("%B %d, %Y %H:%M:%S")
print("Today is: ", now)
print("Hello! Welcome to my ToDo App!")
print("1. Show Todo lists\n2. Add new task\n3. Edit task\n4. Complete task\n5. Exit")

user_choice = ""
todos = []

while True:
    user_choice = input("What do you wanna do: ").capitalize()
    user_choice = user_choice.strip()
    if user_choice.startswith("Add"):
        task = user_choice[4:]
        todos.append(task.capitalize())
    elif user_choice == "Show":
        for index, task in enumerate(todos):
            print(f"{index+1}: {task}")
    elif user_choice.startswith("Edit"):
        number = int(user_choice[5:])
        new_task = input("Enter the edit task: ")
        todos[number-1] = new_task.capitalize()
    elif user_choice.startswith("Complete"):
        number = int(user_choice[9:])
        print(f"The task {todos[number-1]} was completed!")
        todos.pop(number-1)
    elif "Exit" in user_choice:
        print("Bye")
        break
    else:
        print("You write an unknown command.")
