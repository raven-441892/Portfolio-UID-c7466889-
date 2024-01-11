# Write and test a function that determines if a given integer is a prime number. A
# prime number is an integer greater than 1 that cannot be produced by multiplying
# two other integers.

def is_prime(number):  # Function to check if a number is prime
    if number <= 1:  # Check if the number is less than or equal to 1
        print("Please enter a positive integer!")  # Prompt for a positive integer
        return False  # Return False for non-positive integers

    for i in range(2, int(number ** 0.5) + 1):  # Iterate from 2 up to the square root of the number
        if number % i == 0:  # Check if the number is divisible by any value in the range
            return False  # Return False if it's divisible by any number

    return True  # Return True if the number is not divisible by any number other than 1 and itself

num = int(input("Enter an integer to check if it's prime: "))  # Take input from the user
if is_prime(num):  # Check if the input number is prime
    print(f"{num} is a prime number.")  # Display a message indicating the number is prime
else:
    print(f"{num} is not a prime number.")  # Display a message indicating the number is not prime
