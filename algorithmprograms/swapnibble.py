"""
Name     : SwapNibbles.py
Date     : 26/08/2019
Purpose  : read an integer as an Input, convert to Binary and perform the Following functions:
            i. Swap nibbles and find the new number.
            ii. Find the resultant number is the number is a power of 2.

"""


from Utility import utility

#Getting the number from the user
n=int(input("Enter a decimal number : "))

#Calling the function in the BL file
num=utility.swapnibble(n)

#Printing the converted decimal number
print(num)
