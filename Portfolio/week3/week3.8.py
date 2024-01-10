# 8. Modify the "Times Table" again so that the user still enters the number of the table,
# but if this number is negative the table is printed backwards. So entering "-7"
# would produce the Seven Times Table starting at "12 times" down to "0 times".

n = int(input("Enter number between 0 to 12 for the table: "))  # Get user input for the desired table number

if 0 <= n <= 12:  # Check if the entered number is between 0 and 12 inclusive
    for i in range(0, 13):  # Loop through numbers 0 to 12 inclusive
        print(i, "*", n, "=", (i * n))  # Display the result of multiplying each number in the range by the entered number

elif n < 0:  # Check if the entered number is negative
    for i in range(12, -1, -1):  # Loop backward from 12 to 0
        print(i, "*", (-n), "=", (i * (-n)))  # Display the result of multiplying each number in reverse order by the positive value of the entered number

else:
    print("The number you entered is not in between 0 to 12")  # Inform the user if the entered number is outside the specified range
