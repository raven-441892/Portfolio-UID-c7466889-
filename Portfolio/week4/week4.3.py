# 3. Modify your "greetings" program so that the first letter of the name entered is
# always in uppercase with the rest in lowercase. This should happen even if the user
# entered their name differently. So if the user entered arthur, ARTHUR, or even
# arTHur the name should be displayed as Arthur.

def order(name):  # Define a function called order to format the name's first letter as uppercase and the rest as lowercase
    print(f"Greetings, {name.capitalize()}")  # Display the formatted name using capitalize() to ensure the first letter is uppercase and the rest are lowercase

name = input("Enter your name: ")  # Prompt the user to input their name
y = order(name)  # Call the order function to format the name as required
