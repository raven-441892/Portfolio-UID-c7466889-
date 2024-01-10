# 5. Write and test a function that converts a temperature measured in degrees
# centigrade into the equivalent in fahrenheit, and another that does the reverse
# conversion. Test both functions. (Google will find you the formulae).

def intake():  # Define a function called intake to get temperature inputs in both Celsius and Fahrenheit
    cel = float(input("Enter the temperature in Celsius: "))  # Prompt for temperature in Celsius
    fahr = float(input("Enter the temperature in Fahrenheit: "))  # Prompt for temperature in Fahrenheit
    return cel, fahr  # Return the entered temperatures

def cel_to_fahr(cel):  # Define a function to convert Celsius to Fahrenheit
    fah = cel * (9 / 5) + 32  # Convert Celsius to Fahrenheit using the formula
    return fah  # Return the temperature in Fahrenheit

def fahr_to_cel(fahr):  # Define a function to convert Fahrenheit to Celsius
    celc = (fahr - 32) * (5 / 9)  # Convert Fahrenheit to Celsius using the formula
    return celc  # Return the temperature in Celsius

def result(cel, celc, fah, fahr):  # Define a function to display the converted temperatures
    print(f"{cel}°C in Fahrenheit is {fah:.2f}°F")  # Display Celsius to Fahrenheit conversion
    print(f"{fahr}°F in Celsius is {celc:.2f}°C")  # Display Fahrenheit to Celsius conversion

# Main part of the program
cel, fahr = intake()  # Get temperature inputs
fah = cel_to_fahr(cel)  # Convert Celsius to Fahrenheit
celc = fahr_to_cel(fahr)  # Convert Fahrenheit to Celsius
result(cel, celc, fah, fahr)  # Display the converted temperatures


# each function are returning these respective values a=cel, b=celc , c=fah , d= fahr
    




    
    
