"""
process_input.py

Processes the user input in a way that the file system
manager can understand, separating the command, filepath,
and options.
"""

# Kiva Vakharia
# kvakhari@uci.edu
# 23234227


def process_input(user_input: str) -> str:
    """Process input from the user.

    Outputs the initial command, filepath, and additional function
    options within the initial command.

    Returns:
    command: The initial command
    filepath: The filepath to the folder.
    options: Additional functions within the commands.
    """
    if user_input == "Q":
        exit()

    if user_input[0] == 'E' or user_input[0] == 'P':
        command = user_input[0]
        options = user_input[2:]
        filepath = None
        return command, filepath, options

    try:
        if "\\" in user_input:
            split_input = user_input.split("\\")
        elif "/" in user_input:
            split_input = user_input.split("/")

        command = split_input[0][0].strip()
        options = split_input[-1].strip()
    except ValueError as exc:
        raise ValueError("The inputted values are invalid.") from exc

    filepath = ''
    pathname = []

    for i in range(len(split_input)):
        if i in (0, len(split_input) - 1):
            continue

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

    later_options = ["-r", "-f", "-e", "-s", "-n", "-usr", "-pwd", "-bio",
                     "-addpost", "-delpost", "-post", "-posts", "-all"]
    need_more_input = ['-e', '-s', '-n', '-addpost', '-delpost', '-post']

    if "\\" in user_input:
        if split_input[-1][1] != " ":
            split_options = options.split(" ")

            final_file = []

            for i in split_options:
                if i in later_options:
                    break
                if i not in later_options:
                    index = split_options.index(i)
                    final_file.append(split_options[index])

            i = 1
            list_options = []
            while i < len(split_options):
                if split_options[i].startswith('-'):
                    list_options.append(split_options[i])
                    if split_options[i] in need_more_input:
                        i += 1
                        list_options.append(split_options[i])
                i += 1

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
