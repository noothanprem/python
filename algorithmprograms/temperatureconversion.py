"""

Name    : TemperatureConversion.py
Date    : 26/09/2019
Purpose : given the temperature in fahrenheit as input outputs the temperature in Celsius or viceversa

"""



from Utility import utility

#asking the user whether to convert from celsius to Farenheit or from Farenheit to Celsius
n=int(input("Enter 1 for Celsius to Farenheit or 2 for Fareheit to Celsius "))

#Calling the function in the BL file
utility.tempconvert(n)