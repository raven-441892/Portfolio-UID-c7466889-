# Write a program that, when run from the command line, reports how many
# arguments were provided. (Remember that the program name itself is not an
# argument).

import sys  # Import the sys module to access command-line arguments

def arguments_count():  # Define a function to count the command-line arguments
    count = len(sys.argv) - 1  # Calculate the number of command-line arguments provided
    print(f"Number of arguments provided: {count}")  # Display the count of arguments

if __name__ == "__main__":  # Check if the script is being run as the main program
    arguments_count()  # Call the arguments_count function to count the provided arguments
    

#python week5.2.py arg1 arg2 writing it in terminal to access the program