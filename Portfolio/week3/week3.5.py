# 5. Modify your program a final time so that it executes until the user successfully
# chooses a password. That is, if the password chosen fails any of the checks, the
# program should return to asking for the password the first time.
while True:    
    password1 = input("Please enter your new password: ")  # Prompt user for a new password
    password2 = input("Please enter your password again for confirmation: ")  # Prompt for password confirmation
    
    BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']  # List of common bad passwords
    
    if password1.lower() in BAD_PASSWORDS:  # Check if the entered password is in the list of bad passwords
        print("Your password is a common password. Please choose a different one.")  # Prompt to choose a different password
    
    if password1 == password2:  # Check if passwords match
        if 8 <= len(password1) <= 12:  # Ensure password length is between 8 and 12 characters
            print("Password Set")  # Confirm successful password set within length criteria
            break  # Exit the loop as the password meets all criteria
        else:
            print("Password length not in between 8 to 12")  # Report if password length is outside the required range
    else:
        print("Error while password entry")  # Report an error if passwords don't match
