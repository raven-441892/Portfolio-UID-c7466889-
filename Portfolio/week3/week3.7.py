# 7. Modify your "Times Table" program so that the user enters the number of the table
# they require. This number should be between 0 and 12 inclusive.

n = int(input("Enter number between 0 to 12 for the table: "))  # Get user input for the desired table number

if 0 <= n <= 12:  # Check if the entered number is between 0 and 12 inclusive
    for i in range(0, 13):  # Loop through numbers 0 to 12 inclusive
        print(i, "*", n, "=", (i * n))  # Display the result of multiplying each number in the range by the entered number
else:
    print("The number you entered is not in between 0 to 12")  # Inform the user if the entered number is outside the specified range
