"""

Name      : leapyear.py
Date      : 26/08/2019
Purpose   : Determine if the given year is a Leap Year or not.

"""

from Utility import utility

#taking the year from the user
y = int(input("Enter the year : "))

#calling the function in the BL file
utility.leap(y)