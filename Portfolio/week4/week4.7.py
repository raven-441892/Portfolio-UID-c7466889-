# 7. Write a program that reads 6 temperatures (in the same format as before), and
# displays the maximum, minimum, and mean of the values.
# Hint: You should know there are built-in functions for max and min. If you hunt, you
# might also find one for the mean.

def intake():  # Define a function called intake to get 6 temperature inputs in Celsius
    celcius = []  # Create an empty list to store the temperatures
    for i in range(6):  # Loop six times to get six temperature inputs
        cel = float(input("Enter the temperature in Celsius: "))  # Prompt for temperature in Celsius
        celcius.append(cel)  # Add each temperature to the list
    return celcius  # Return the list of temperatures

def maximum(celcius):  # Define a function to find the maximum temperature
    maxi = max(celcius)  # Find the maximum temperature using the max function
    return maxi  # Return the maximum temperature

def minimum(celcius):  # Define a function to find the minimum temperature
    mini = min(celcius)  # Find the minimum temperature using the min function
    return mini  # Return the minimum temperature

def mean_of_temp(celcius):  # Define a function to find the mean of the temperatures
    total = sum(celcius)  # Calculate the total sum of all temperatures
    N = len(celcius)  # Get the number of temperatures
    mean = total / N  # Calculate the mean by dividing the total sum by the number of temperatures
    return mean  # Return the mean temperature

def display(maxi, mini, mean):  # Define a function to display the calculated values
    print(f"The maximum temperature is {maxi:.2f}°C")  # Display the maximum temperature
    print(f"The minimum temperature is {mini:.2f}°C")  # Display the minimum temperature
    print(f"The mean of all 6 temperatures is {mean:.2f}°C")  # Display the mean temperature

a=intake()  # Get 6 temperature inputs
b=maximum(a) # Find the maximum temperature
c=minimum(a) # Find the minimum temperature
d=mean_of_temp(a) # Find the mean temperature
z=display(b,c,d)  # Display the calculated values




    
    
        
    
        