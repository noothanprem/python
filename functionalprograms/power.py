"""

Name    : Power.py
Date    : 26/08/2019
Purpose : Take a command-line argument N and print a table of the powers of 2 that are less than or equal to 2^N.

"""


from Utility import utility

# getting the number from the user
n = int(input("Enter the number : "))

# Checking whether the given number is less than or equal to 30 or not
# If it is greater than 30, prompt the user to enter a number less than 31
if (n > 30):
    print("Enter a number below 31")
# if the number is below 31, call the function in the BL file
else:
    utility.pow1(n)

