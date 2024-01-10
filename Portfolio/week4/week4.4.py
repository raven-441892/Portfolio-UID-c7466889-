# 4. When processing data it is often useful to remove the last character from some
# input (it is often a newline). Write and test a function that takes a string parameter
# and returns it with the last character removed. (If the string contains one or fewer
# characters, return it unchanged.)

def remove_last(string):  # Define a function called remove_last to remove the last character from a string
    if len(string) >= 1:  # Check if the length of the string is greater than or equal to 1
        remove = string[0:-1]  # Remove the last character by slicing the string
        return remove  # Return the modified string with the last character removed
    else:
        return string  # Return the input string unchanged if its length is one or fewer characters

string = input("Enter a string: ")  # Prompt the user to input a string
removed_string = remove_last(string)  # Call the remove_last function to remove the last character from the input string
print(removed_string)  # Display the modified string with the last character removed
