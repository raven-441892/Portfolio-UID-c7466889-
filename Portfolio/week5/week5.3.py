# Write a program that takes a bunch of command-line arguments, and then prints
# out the shortest. If there is more than one of the shortest length, any will do.
# Hint: Don't overthink this. A good way to find the shortest is just to sort them

import sys

if __name__ == "__main__":
    arguments = sys.argv[1:]  # removes the first name as it includes script name
    if arguments:
        shortest = arguments[0]  # puts shortest as the first argument
        for arg in arguments[1:]:
            if len(arg) < len(shortest):
                shortest = arg  # changes shortest if a shorter argument is found
        print(f"The shortest argument is: {shortest}")
    else:
        print("No arguments provided.")


#python week5.3.py abc ldskjg sdsf ksfj write in terminal with diff command line arguments for accessing this code