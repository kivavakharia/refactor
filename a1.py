"""
a1.py

Starting point of the File System Manager.
"""

# Kiva Vakharia
# kvakhari@uci.edu
# 23234227

from process_input import process_input
from commands import Commands


def send_command(command: str, filepath: str, options: str):
    """
    Sends the command to a command-processing function.
    """
    obj = Commands(filepath, options)
    if command == "L":
        return obj.l_command()

    elif command == "C":
        return obj.c_command()

    elif command == "R":
        return obj.r_command()

    elif command == "D":
        return obj.d_command()


def main(user_input):
    """Run the functions.
    
    Raise error if input is in the incorrect format
    """
    try:
        if user_input[0] == "Q":
            exit()

        if len(user_input) < 2:
            raise ValueError

        command, filepath, options = process_input(user_input)
        send_command(command, filepath, options)

    except UnboundLocalError:
        print("ERROR")
    except ValueError:
        print("ERROR")


if __name__ == "__main__":
    user_input = ''

    while user_input != "Q":
        user_input = input()
        main(user_input)
