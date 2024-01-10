# 6. Write a program that takes a centigrade temperature and displays the equivalent in
# fahrenheit. The input should be a number followed by a letter C. The output should
# be in the same format.

def intake():  # Define a function called intake to get temperature input in Celsius format
    cel = input("Enter the temperature in Celsius with 'C' behind: ")  # Prompt for temperature in Celsius with 'C' at the end
    return cel  # Return the entered temperature

def cel_to_fahr(cel):  # Define a function to convert Celsius to Fahrenheit
    y = cel[-1]  # Extract the last character of the input to check if it's 'C' or 'c'
    x = float(cel[0:-1])  # Extract the numeric part of the input for conversion
    if y == "C" or y == "c":  # Check if the last character is 'C' or 'c'
        fah = x * (9 / 5) + 32  # Convert Celsius to Fahrenheit using the formula
        return fah  # Return the temperature in Fahrenheit if the input format is correct

def result(cel, fah):  # Define a function to display the converted temperature
    print(f"{cel} in Fahrenheit is {fah:.2f}°F")  # Display the temperature in Fahrenheit

a = intake()  # Get temperature input
b = cel_to_fahr(a)  # Convert Celsius to Fahrenheit
if b is not None:  # Check if conversion was successful
    result(a, b)  # Display the converted temperature
else:
    print("Invalid input. Please provide temperature in the correct format.")  # Inform about incorrect input format


#a takes cel and b takes fah
