# Write and test a function that takes a string as a parameter and returns a sorted list
# of all the unique letters used in the string. So, if the string is cheese, the list
# returned should be ['c', 'e', 'h', 's'].

def unique_character(string):  # Function to find unique characters in a string and return a sorted list
    collect_unique = set(string)  # Convert the string to a set to collect unique characters
    ordered = sorted(collect_unique)  # Sort the unique characters
    return ordered  # Return the sorted list of unique characters

def output(string, ordered):  # Function to display the sorted list of unique letters
    print(f"The sorted list of unique letters in '{string}' is {ordered}")  # Display the sorted list

string = input("Enter a string for its sorted list of unique letters: ")  # Take input from the user
result = unique_character(string)  # Find unique characters and sort them
display=output(string,result)  # Display the sorted list of unique letters



