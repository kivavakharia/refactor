# Assignment 1

# Kiva Vakharia
# kvakhari@uci.edu
# 23234227

from pathlib import *


def process_input(user_input):
    """Process input from the user.

    Outputs the initial command, filepath, and additional function
    options within the initial command.

    Parameters:
    - user_input (str): Input from the user.

    Returns:
    command: The initial command
    filepath: The filepath to the folder.
    options: Additional functions within the commands.
    """
    if user_input == "Q":
        exit()

    if "\\" in user_input:
        split_input = user_input.split("\\")
    elif "/" in user_input:
        split_input = user_input.split("/")

    command = split_input[0][0].strip()
    options = split_input[-1].strip()

    filepath = ''
    pathname = []

    for i in range(len(split_input)):
        if (i == 0) or (i == (len(split_input) - 1)):
            continue

        later_options = ["-r", "-f", "-e", "-s", "-n"]

        if "\\" in user_input:
            if i == 1:
                if split_input[1][-1] != " ":
                    input_beginning = split_input[0]
                    split_command = input_beginning.split(" ")
                    pathname.append(split_command[1])

            pathname.append(split_input[i])

        if "/" in user_input:
            filepath += '/'
            filepath += split_input[i]

    if "\\" in user_input:
        if split_input[-1][1] != " ":
            split_options = options.split(" ")

            final_file = []

            for i in split_options:
                if i in later_options:
                    break
                elif i not in later_options:
                    index = split_options.index(i)
                    final_file.append(split_options[index])

            list_options = []
            for i in split_options:
                if i in later_options:
                    list_options.append(i)
                    index = split_options.index(i)
            
            if len(split_options) > (index + 1):
                list_options.append(split_options[index + 1])

            options = ' '.join(list_options)
            last_filename = ' '.join(final_file)

        filepath = '\\'.join(pathname)
        filepath += '\\'
        filepath += last_filename

        if len(split_input) == 2:
            input_beginning = split_input[0]
            split_command = input_beginning.split(" ")
            filepath = split_command[1] + '\\' + filepath

    if "/" in user_input:
        filepath += '/'

    return command, filepath, options


def recursive(filepath, options):
    """
    Recursively print the contents within a directory.

    Parameters:
    - filepath (str): A filepath to the directory.
    """
    directory = Path(filepath)

    for i in directory.iterdir():
        if i.is_file():
            print(i)

    for i in directory.iterdir():
        if i.is_dir() and ("-f" not in options):
            print(i)
            recursive(i, options)


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


def main(user_input):
    """Run the functions."""
    if user_input[0] == "Q":
        exit()

    if len(user_input) < 2:
        print("ERROR")
        return
    
    command, filepath, options = process_input(user_input)
    # print(f'Command: {command}, Filepath: {filepath}, Options: {options}')

    if command == "L":
        l_command(filepath, options)

    elif command == "C":
        print(c_command(filepath, options))

    elif command == "R":
        print(r_command(filepath))

    elif command == "D":
        print(d_command(filepath))


if __name__ == "__main__":
    user_input = ''

    while user_input != "Q":
        user_input = input()
        main(user_input)
