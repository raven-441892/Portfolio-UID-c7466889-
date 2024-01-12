# The Unix nl command prints the lines of a text file with a line number at the start
# of each line. (It can be useful when printing out programs for dry runs or white-box
# testing). Write an implementation of this command. It should take the name of the
# files as a command-line argument.

import sys

def nl(file_name):
    try:
        with open(file_name, 'r') as file:
            line_number = 1
            for line in file:
                print(f"{line_number}\t{line}", end='')
                line_number += 1
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")

if len(sys.argv) < 2:
    print("Please provide a file name as a command-line argument.")
else:
    file_name = sys.argv[1]
    nl(file_name)
    
#python week8.1.py your_file.txt

