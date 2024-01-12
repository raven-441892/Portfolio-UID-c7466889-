# The Unix diff command compares two files and reports the differences, if any.
# Write a simple implementation of this that takes two file names as command-line
# arguments and reports whether or not the two files are the same. (Define "same" as
# having the same contents.)

import sys

def file_contents_equal(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        return f1.read() == f2.read()

def diff(file1, file2):
    try:
        if file_contents_equal(file1, file2):
            print("The files have the same contents.")
        else:
            print("The files have different contents.")
    except FileNotFoundError as e:
        print(e)

if len(sys.argv) < 3:
    print("Please provide two file names as command-line arguments.")
else:
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    diff(file1, file2)
    
#python week8.2.py file1.txt file2.txt


