"""
a1.py

Starting point of the File System Manager.
"""

# Kiva Vakharia
# kvakhari@uci.edu
# 23234227

from pathlib import Path
from process_input import process_input



def only_files(filepath):
    """
    Print only the files within a given directory.

    Parameters:
    - filepath (str): A filepath to the directory.
    """
    directory = Path(filepath)
    for i in directory.iterdir():
        if i.is_file():
            print(i)


def only_filename(filepath, options):
    """
    Print only the files with a specific filename within a given directory.

    Parameters:
    - filepath (str): A filepath to the directory.
    - options (str): Stores additional information to achieve the goal.
    """
    list_options = options.split(" ")
    filename = list_options[1]

    directory = Path(filepath)
    for i in directory.iterdir():
        if i.name == filename:
            print(i)


def only_extension(filepath, options):
    """
    Print only the files with a specific suffix within a given directory.

    Parameters:
    - filepath (str): A filepath to the directory.
    - options (str): Stores additional information to achieve the goal.
    """
    list_options = options.split(" ")
    extension = list_options[-1]

    directory = Path(filepath)
    for i in directory.iterdir():
        if i.suffix == extension:
            print(i)


def l_command(filepath, options):
    """
    List the contents within a given directory.

    Parameters
    - filepath (str): A filepath to the directory.
    - options (str): Stores additional information to achieve the goal.
    """

    if all(option not in options for option in ("-r", "-e", "-f", "-s")):
        directory = Path(filepath)
        files = []
        folders = []
        for i in directory.iterdir():
            if i.is_dir():
                folders.append(i)
            elif i.is_file():
                files.append(i)

        for file in files:
            print(file)
        for folder in folders:
            print(folder)

    if "-r" in options:
        if all(option not in options for option in ("-e", "-f", "-s")):
            directory = Path(filepath)

            for i in directory.iterdir():
                if i.is_file():
                    print(i)

            for i in directory.iterdir():
                if i.is_dir():
                    print(i)
                    l_command(i, options)
        
        elif "-f" in options:
            directory = Path(filepath)

            for i in directory.iterdir():
                if i.is_file():
                    print(i)
            
            for i in directory.iterdir():
                if i.is_dir():
                    l_command(i, options)

        elif "-e" in options:
            directory = Path(filepath)
            list_options = options.split(" ")
            extension = list_options[-1]
            extension = "." + extension

            for i in directory.iterdir():
                if i.is_file() and (i.suffix == extension):
                    print(i)
            
            for i in directory.iterdir():
                if i.is_dir():
                    l_command(i, options)

        elif "-s" in options:
            directory = Path(filepath)
            list_options = options.split(" ")
            filename = list_options[-1]

            for i in directory.iterdir():
                if i.is_file() and (i.name == filename):
                    print(i)
            
            for i in directory.iterdir():
                if i.is_dir():
                    l_command(i, options)

    if "-e" in options:
        only_extension(filepath, options)

    if "-f" in options:
        if "-r" not in options:
            only_files(filepath)

    if "-s" in options:
        only_filename(filepath, options)


def c_command(filepath, options):
    """Create a file at the specified filepath with the provided filename.

    Parameters:
    - filepath (str): A filepath to the directory.
    - options (str): Stores additional information to achieve the goal.

    Returns:
    filepath: The filepath of the newly created file.
    """

    split = options.split(" ")
    filename = split[1]

    if "\\" in filepath:
        filename = "\\" + filename

    filename += ".dsu"
    filepath += filename
    Path(filepath).touch()

    return filepath


def d_command(delete_filepath):
    """Delete the file at the specified filepath.

    Parameters:
    - delete_filepath (str): A filepath to the directory to be deleted.

    Returns:
    delete_statement: A statement that the given filepath was deleted.
    """
    if delete_filepath[-4:] != ".dsu":
        return "ERROR"

    Path.unlink(delete_filepath)
    delete_statement = delete_filepath + " DELETED"
    return delete_statement


def r_command(read_filepath):
    """Read the file located at the specified filepath.

    Parameters:
    - filepath (str): A filepath to the directory to be read.

    Returns:
    file_contents: The text written within the file.
    """
    filepath = Path(read_filepath)
    file_contents = Path(read_filepath).read_text()
    
    if filepath.suffix != ".dsu":
        return "ERROR"
    
    if file_contents == "":
        return "EMPTY"

    return file_contents

def send_command(command, filepath, options):
        if command == "L":
            l_command(filepath, options)

        elif command == "C":
            print(c_command(filepath, options))

        elif command == "R":
            print(r_command(filepath))

        elif command == "D":
            print(d_command(filepath))


def main(user_input):
    """Run the functions."""
    if user_input[0] == "Q":
        exit()

    if len(user_input) < 2:
        print("ERROR")
    
    try:
        command, filepath, options = process_input(user_input)
    except UnboundLocalError:
        print("ERROR")
    # print(f'Command: {command}, Filepath: {filepath}, Options: {options}')

    try:
        send_command(command, filepath, options)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    user_input = ''

    while user_input != "Q":
        user_input = input()
        main(user_input)
