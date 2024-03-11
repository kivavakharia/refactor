"""
commands.py

This module holds all the functionality behind the
comands available in the File Management System.
"""

# Kiva Vakharia
# kvakhari@uci.edu
# 23234227


from pathlib import Path


def c_command(filepath, options) -> None:
    """
    Create a file at the specified filepath with the provided filename.
    """
    split = options.split(" ")
    filename = split[1]

    if "\\" in filepath:
        filename = "\\" + filename

    filename += ".dsu"
    filepath += filename
    Path(filepath).touch()

    print(filepath)


def l_command(filepath, options):
    """
    List the contents within a given directory.
    """            

    def only_extension(filepath, options):
        """
        Print only the files with a specific suffix within a given directory.
        """
        list_options = options.split(" ")
        extension = list_options[-1]

        directory = Path(filepath)
        for i in directory.iterdir():
            if i.suffix == extension:
                print(i)

    def only_filename(filepath, options):
        """
        Print only the files with a specific filename within a given directory.
        """
        list_options = options.split(" ")
        filename = list_options[1]

        directory = Path(filepath)
        for i in directory.iterdir():
            if i.name == filename:
                print(i)

    def only_files(filepath):
        """
        Print only the files within a given directory.
        """
        directory = Path(filepath)
        for i in directory.iterdir():
            if i.is_file():
                print(i)

    valid_options = ("-r", "-e", "-f", "-s")
    if all(option not in options for option in valid_options):
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
        valid = ("-e", "-f", "-s")
        if all(option not in options for option in valid):
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


def d_command(filepath) -> None:
    """
    Delete the file at the specified filepath.
    """
    if filepath[-4:] != ".dsu":
        return "ERROR"

    Path.unlink(filepath)
    delete_statement = filepath + " DELETED"
    print(delete_statement)


def r_command(filepath) -> None:
    """
    Read the file located at the specified filepath.
    """
    filepath = Path(filepath)
    file_contents = Path(filepath).read_text()

    if filepath.suffix != ".dsu":
        print("ERROR")

    if file_contents == "":
        print("EMPTY")

    print(file_contents)
