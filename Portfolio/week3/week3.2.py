# 2. Write a program that simulates the way in which a user might choose a password.
# The program should prompt for a new password, and then prompt again. If the two
# passwords entered are the same the program should say "Password Set" or
# similar, otherwise it should report an error.

password1 = input("Please enter your new password: ")  # Prompt user for a new password
password2 = input("Please enter your password again for confirmation: ")  # Prompt for password confirmation
if password1 == password2:  # Check if passwords match
    print("Password Set")  # Confirm successful password set
else:
    print("Error while password entry")  # Report an error if passwords don't match
