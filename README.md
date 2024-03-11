# Information Retrieval: Assignment Refactor

In my refactor of Assignment 1, I have completely reorganized my code to
make it more readable and organized by dividing the original code into three modules.
The first module, a1.py, contains the starting point of the code and one function that
processes functionality. My main function calls the other two modules: ui.py, which
processes the user input in a way that the system understands, and commands.py, which
has all the functions that run command functionality.

In terms of implementing course concepts, I have made the send_command function, which is a
higher-order function that returns functions from the commands.py module. I have also impemented
nested functions within my L command function under commands.py.

Team Members:
Kiva Vakharia