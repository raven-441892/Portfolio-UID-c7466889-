# Last week you wrote a program that processed a collection of temperature readings
# entered by the user and displayed the maximum, minimum, and mean. Create a
# version of that program that takes the values from the command-line instead. Be
# sure to handle the case where no arguments are provided!


import sys

def maximum(celcius):  # Function to find the maximum temperature
    maxi = max(celcius)
    return maxi

def minimum(celcius):  # Function to find the minimum temperature
    mini = min(celcius)
    return mini

def mean_of_temp(celcius):  # Function to find the mean of the temperatures
    total = sum(celcius)
    N = len(celcius)
    mean = total / N
    return mean

def display(maxi, mini, mean):  # Function to display the calculated values
    print(f"The maximum temperature is {maxi:.2f}C")
    print(f"The minimum temperature is {mini:.2f}C")
    print(f"The mean of all temperatures is {mean:.2f}C")

if __name__ == "__main__":
    arguments = sys.argv[1:]  # Get command-line arguments excluding the script name
    if len(arguments) < 6:  # Check if there are at least 6 temperature values provided
        print("Please provide at least 6 temperature values.")
    else:
        temperatures = [float(temp) for temp in arguments]  # Convert arguments to float temperatures
        max_temp = maximum(temperatures)  # Find the maximum temperature
        min_temp = minimum(temperatures)  # Find the minimum temperature
        mean_temp = mean_of_temp(temperatures)  # Find the mean temperature
        display(max_temp, min_temp, mean_temp)  # Display the calculated values
 
#python week5.5.py 56 23 84 92 67 10 52 type it in terminal for code function