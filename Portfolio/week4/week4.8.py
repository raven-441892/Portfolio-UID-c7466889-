# 8. Modify the previous program so that it can process any number of values. The input
# terminates when the user just pressed "Enter" at the prompt rather than entering a
# value.

def intake():  # Define a function to receive temperatures until the user presses Enter
    celcius = []  # Create an empty list to store the temperatures
    while True:  # Infinite loop to receive temperatures until the user stops
        user = input("Enter the temperature in Celsius or press Enter to stop: ")  # Prompt user for input
        if user == "":  # Check if user pressed Enter without entering a temperature
            break  # Exit the loop if Enter was pressed without entering a value
        cel = float(user)  # Convert the user input to a float (temperature)
        celcius.append(cel)  # Add the temperature to the list
    return celcius  # Return the list of entered temperatures

def maximum(celcius):  # Define a function to find the maximum temperature
    maxi = max(celcius)  # Find the maximum temperature using the max function
    return maxi  # Return the maximum temperature

def minimum(celcius):  # Define a function to find the minimum temperature
    mini = min(celcius)  # Find the minimum temperature using the min function
    return mini  # Return the minimum temperature

def mean_of_temp(celcius):  # Define a function to find the mean of the temperatures
    if celcius:  # Check if the list is not empty
        total = sum(celcius)  # Calculate the total sum of all temperatures
        N = len(celcius)  # Get the number of temperatures
        mean = total / N  # Calculate the mean by dividing the total sum by the number of temperatures
        return mean  # Return the mean temperature
    else:
        return 0  # Return 0 if no temperatures were entered

def display(maxi, mini, mean):  # Define a function to display the calculated values
    print(f"The maximum temperature is {maxi:.2f}°C")  # Display the maximum temperature
    print(f"The minimum temperature is {mini:.2f}°C")  # Display the minimum temperature
    print(f"The mean of all temperatures is {mean:.2f}°C")  # Display the mean temperature

# Main part of the program
a=intake()  # Get temperatures until the user stops entering

if a:   # Check if temperatures were entered
    b=maximum(a)    # Find the maximum temperature
    c=minimum(a)    # Find the minimum temperature
    d=mean_of_temp(a)   # Find the mean temperature
    z=display(b,c,d)  # Display the calculated values
    
else:
    print("No temperature entered")     # Inform if no temperatures were entered
