# Write and test three functions that each take two words (strings) as parameters and
# return sorted lists (as defined above) representing respectively:
# Letters that appear in at least one of the two words.
# Letters that appear in both words.
# Letters that appear in either word, but not in both.
# Hint: These could all be done programmatically, but consider carefully what topic we
# have been discussing this week! Each function can be exactly one line.

def letters_in_either(word1, word2):  # Function to find letters in either of the two words
    in_either = sorted(set(word1) | set(word2))  # Find letters appearing in either word
    return in_either  # Return the sorted list

def letters_in_both(word1, word2):  # Function to find letters in both words
    in_both = sorted(set(word1) & set(word2))  # Find letters appearing in both words
    return in_both  # Return the sorted list

def letters_in_either_not_both(word1, word2):  # Function to find letters in either word but not in both
    in_either = set(word1) | set(word2)  # Find letters appearing in either word
    in_both = set(word1) & set(word2)  # Find letters appearing in both words
    in_either_not_both = in_either - in_both  # Find letters appearing in either but not both
    return sorted(in_either_not_both)  # Return the sorted list

def output(word1, word2, in_either, in_both, in_either_not_both):  # Function to display the results
    print(f"Letters that appear in at least one of the two words '{word1}' and '{word2}' are {in_either}")
    print(f"Letters that appear in both words '{word1}' and '{word2}' are {in_both}")
    print(f"Letters that appear in either word, but not in both words '{word1}' and '{word2}' are {in_either_not_both}")

a = input("Enter first word: ")  # Take input of the first word from the user
b = input("Enter second word: ")  # Take input of the second word from the user
x = letters_in_either(a, b)  # Find letters in either word
y = letters_in_both(a, b)  # Find letters in both words
z = letters_in_either_not_both(a, b)  # Find letters in either word but not in both
display=output(a, b, x, y, z)  # Display the results



