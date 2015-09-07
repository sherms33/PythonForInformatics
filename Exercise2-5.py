#Exercise 2-5
#Write a program which prompts the user for a Celsius temperature,
#convert the temperature to Fahrenheit, and print out the
#converted temperature

temp_celsius = float(raw_input('Enter temperature in Celsius: '))
temp_fahrenheit = (temp_celsius * 1.8) + 32
print temp_fahrenheit
