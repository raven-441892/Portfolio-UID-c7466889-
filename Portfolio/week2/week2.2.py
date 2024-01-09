# 2. Write a program that prompts a user to enter a temperature in Celsius, and then
# displays the corresponding temperature in Fahrenheit, like so:
#     Enter a temperature in Celsius: 32.5
#     32.5C is equivalent to 90.5F.

#takes temperature in celcius and converts it into fahrenheit then displays in a format
cel= float(input("Enter temperature in celcius: "))
fahr= cel*(9/5)+32
print(f"{cel}C is equivalent to {fahr}F.")