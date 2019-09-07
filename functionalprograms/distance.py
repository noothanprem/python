"""

Name     : distance.py
Date     : 26/08/2019
Purpose  :  Prints the distance between the two points

"""

from Utility import utility

while True:
    try:
        #Getting the values of x and y from the user
        x = int(input("Enter the value for x : "))
        y = int(input("Enter the value for y : "))
        # calling the dis() function in the utility class
        distance = utility.dis(x, y)
        print("The Eucledian distance is : ", distance)
        break
    except ValueError:
        print("Please enter numbers only")


