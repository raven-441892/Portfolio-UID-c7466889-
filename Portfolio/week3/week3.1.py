# 1. Modify your greeting program so that if the user does not enter a name (i.e. they
# just press enter), the program responds "Hello, Stranger!". Otherwise it should print
# a greeting with their name as before.

name = input("Enter your name: ")  # Get user's input for their name
if name == "":  # Check if the name is empty
    print("Hello, Stranger!")  # Print a default greeting for no input
else:
    print(f"Hello, {name}")  # Print a personalized greeting with the entered name

