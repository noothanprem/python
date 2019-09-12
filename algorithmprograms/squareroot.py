"""

Name    : SquareRoot.py
Date    : 26/08/2019
Purpose : compute the square root of a nonnegative number c given in the input using Newton's method:

"""

from Utility import utility

while True:
    try:
        #Getting the number from the user
        c=int(input("Enter a non-negative number : "))
        if(c < 0):
            print("Enter Positive Integers only")
            continue
        break
    except ValueError:
        print("Enter integers only")
        continue

#Calling the function in the BL file
t=utility.sqrt(c)

#printing the square root of the number
print("Square root is : ",t)