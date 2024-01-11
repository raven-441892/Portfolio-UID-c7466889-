# 1. Write a function that accepts a positive integer as a parameter and then returns a
# representation of that number in binary (base 2).
# Hint: This is in many ways a trick question. Think!

def to_binary(number):  # Function to convert a positive integer to binary
    if number <= 0:  # Check if the number is not positive
        return "Please enter a positive integer!"  # Return a message for non-positive numbers

    binary = ""  # Initialize an empty string to store the binary representation
    while number > 0:  # Loop until the number becomes zero
        binary = str(number % 2) + binary  # Get the remainder and build the binary representation
        number = number // 2  # Update the number by integer division to get the next digit

    return binary if binary else "0"  # Return the binary representation or '0' if the input was 0

def output(number, binary):  # Function to display the output
    print(f"The binary form of {number} is {binary}")  # Display the number and its binary representation

num = int(input("Enter a positive integer for its binary form: "))  # Take input from the user
result = to_binary(num)  # Convert the input number to its binary representation
display= output(num, result)  # Display the result
