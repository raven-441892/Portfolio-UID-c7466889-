Task 3

User Account Management System
This Python script provides functionalities for managing user accounts, including adding users, deleting users, and changing passwords. 
It utilizes a text file, passwd.txt, to store user account information.

Functionality Overview
1. Add User Functionality
The add_user function allows adding new users to the passwd.txt file. It verifies if the entered username already exists, requires usernames
to be in lowercase, encrypts passwords using ROT_13, and writes the new user information to the file.

2. Delete User Functionality
The del_user function enables deleting existing users from the passwd.txt file. It checks for the existence of the entered username and its password,
encrypts the password using ROT_13 for comparison, and updates the file after removing the specified user.

3. Login Functionality
The login_user function manages user login by checking the provided username and password against the passwd.txt file. It encrypts the password using
ROT_13 for comparison and grants or denies access based on matching credentials.

4. Change Password Functionality
The change_pass function allows changing passwords for existing users in the passwd.txt file. It verifies the current password, encrypts it using ROT_13
for comparison, replaces the old password with the new encrypted password, and updates the file accordingly.

Usage
Ensure Python is installed on your system.
Run each function separately by executing the corresponding script segment.
Example:
python add_user.py passwd.txt
Ensure to replace add_user.py with the respective script name for each function.

Follow the on-screen prompts for each function:
Add User: Enter a new username, real name, and password.
Delete User: Enter the username and its password for deletion.
Login: Enter the username and its password for login verification.
Change Password: Enter the username, current password, new password, and confirmation.
