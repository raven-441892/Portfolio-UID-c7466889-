# 3. Modify your previous program so that the password must be between 8 and 12
# characters (inclusive) long.
password1 = input("Please enter your new password: ")  # Prompt user for a new password
password2 = input("Please enter your password again for confirmation: ")  # Prompt for password confirmation
if password1 == password2:  # Check if passwords match
    if 8 <= len(password1) <= 12:  # Ensure password length is between 8 and 12 characters
        print("Password Set")  # Confirm successful password set within length criteria
    else:
        print("Password length not in between 8 to 12")  # Report if password length is outside the required range
else:
    print("Error while password entry")  # Report an error if passwords don't match
