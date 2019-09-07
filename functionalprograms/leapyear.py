"""

Name      : leapyear.py
Date      : 26/08/2019
Purpose   : Determine if the given year is a Leap Year or not.

"""

from Utility import utility

while True:
    try:
        #taking the year from the user
        y = int(input("Enter the year : "))
        s1=str(y)
        if(len(s1) != 4):
            print("Please enter a 4 digit year")
        else:
            #calling the function in the BL file
            utility.leap(y)
            break
    except ValueError:
        print("Please Enter a number only")