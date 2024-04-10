FILEPATH = r"C:\Users\bunny\OneDrive\Desktop\Python\tasks.txt"




def get_todos(filepath= FILEPATH):
    """ Read a text file and return the list
    of do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
        return todos_local


def write_todos(todos_arg,filepath = FILEPATH):
    """Write do to items in the text file."""
    with open(filepath,'w') as file:
        file.writelines(todos_arg)