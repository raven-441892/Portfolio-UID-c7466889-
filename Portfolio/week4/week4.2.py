# Write a function that has a single string as its parameter, and returns the number of
# uppercase letters, and the number of lowercase letters in the string. Test the
# function with a short program.

def counting(word):  # Define a function called counting that counts uppercase and lowercase letters in a string
    up = 0  # Initialize the count of uppercase letters
    low = 0  # Initialize the count of lowercase letters
    
    for letter in word:  # Loop through each character in the input string
        if letter.isupper():  # Check if the character is uppercase
            up += 1  # Increment the count of uppercase letters
        elif letter.islower():  # Check if the character is lowercase
            low += 1  # Increment the count of lowercase letters
            
    return up, low  # Return the counts of uppercase and lowercase letters as a tuple

word = input("Enter a single string/word: ")  # Prompt the user to input a string
up, low = counting(word)  # Call the counting function to get counts of uppercase and lowercase letters

# Display the counts of uppercase and lowercase letters in the input string
print(f"The number of uppercase letters in the string '{word}' is {up}")
print(f"The number of lowercase letters in the string '{word}' is {low}")
