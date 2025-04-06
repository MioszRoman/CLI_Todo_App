print("Hello! Welcome to my ToDo App!")
print("1. Show Todo lists\n2. Add new task\n3. Edit task\n4. Complete task\n5. Exit")

todos = []

while True:
    user_choice = input("What do you wanna do: ").capitalize()
    if user_choice == "Add":
        task = input("What is task you wanna add: ")
        todos.append(task.capitalize())
    elif user_choice == "Show":
        for index, task in enumerate(todos):
            print(f"{index+1}: {task}")
    elif user_choice == "Edit":
        number = int(input("Which task do you wanna edit: "))
        new_task = input("Enter the edit task: ")
        todos[number-1] = new_task.capitalize()
    elif user_choice == "Complete":
        number = int(input("Which task do you wanna complete: "))
        print(f"The task {todos[number-1]} was completed!")
        todos.pop(number-1)
    elif user_choice == "Exit":
        print("Bye")
        break
