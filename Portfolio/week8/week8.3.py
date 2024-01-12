# The Unix grep command searches a file and outputs the lines in the file that
# contain a certain pattern. Write an implementation of this. It will take two
# command-line arguments: the first is the string to look for, and the second is the
# file name. The output should be the lines in the file that contain the string.

import sys

def grep(pattern, file_name):
    try:
        with open(file_name, 'r') as file:
            for line in file:
                if pattern in line:
                    print(line, end='')
    except FileNotFoundError as e:
        print(e)

if len(sys.argv) < 3:
    print("Please provide a search pattern and a file name as command-line arguments.")
else:
    search_pattern = sys.argv[1]
    file_name = sys.argv[2]
    grep(search_pattern, file_name)

#python week8.3.py search_pattern file_name.txt
