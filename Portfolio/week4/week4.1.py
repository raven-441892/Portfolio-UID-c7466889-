# 1. Functions are often used to validate input. Write a function that accepts a single
# integer as a parameter and returns True if the integer is in the range 0 to 100
# (inclusive), or False otherwise. Write a short program to test the function.

def validate(num):  # Define a function called validate that accepts an integer parameter 'num'
    if 0 <= num <= 100:  # Check if the integer is in the range 0 to 100 (inclusive)
        return True  # Return True if the number is within the specified range
    else:
        return False  # Return False if the number is outside the specified range

y = validate(7)  # Test the validate function with the integer 7
print(y)  # Print the result of the validation (True or False)
