def get_todos(filepath="todos.txt"):
    """This function read todos from a file and return them."""
    with open(filepath, "r") as file_local:
        local_todos = file_local.readlines()
    return local_todos

def write_todos(local_todos, filepath="todos.txt"):
    """Write the todos to a file with extention .txt"""
    with open(filepath, "w") as file_local:
        file_local.writelines(local_todos)