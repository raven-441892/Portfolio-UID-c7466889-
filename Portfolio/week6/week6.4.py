# Computers are commonly used in encryption. A very simple form of encryption
# (more accurately "obfuscation") would be to remove the spaces from a message
# and reverse the resulting string. Write, and test, a function that takes a string
# containing a message and "encrypts" it in this way

def in_value():  # Function to take input string for encryption
    string = input("Enter a string for encryption: ")  # Take input from the user
    return string  # Return the input string

def encryption(string):  # Function to encrypt the input string
    encrypt = string.replace(" ", "")  # Remove spaces from the input string
    encrypt_message = encrypt[::-1]  # Reverse the resulting string
    return encrypt_message  # Return the encrypted message

def output(encrypt_message):  # Function to display the encrypted message
    print(f"The encrypted message of the given string is {encrypt_message}")  # Display the encrypted message

input_str = in_value()  # Take input string for encryption
encrypted = encryption(input_str)  # Encrypt the input string
display=output(encrypted) # Display the encrypted message


               