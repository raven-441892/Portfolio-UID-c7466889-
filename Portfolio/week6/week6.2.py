# 2. Write and test a function that takes an integer as its parameter and returns the
# factors of that integer. (A factor is an integer which can be multiplied by another to
# yield the original).

def factor(number):  # Function to find factors of an integer
    if number < 1:  # Check if the number is not positive
        return "Please enter a positive integer!"  # Return a message for non-positive numbers

    factors = []  # Initialize an empty list to store factors
    for i in range(1, number + 1):  # Iterate from 1 to the number inclusive
        if number % i == 0:  # Check if 'i' is a factor of the number
            factors.append(i)  # If 'i' is a factor, add it to the list of factors
    return factors  # Return the list of factors

def output(number, factors):  # Function to display the output
    print(f"The factors of {number} are {factors}")  # Display the number and its factors

num = int(input("Enter a positive integer to find its factors: "))  # Take input from the user
fact = factor(num)  # Get the factors of the input number
display=output(num,fact) # Display the factors of the input number


        
        