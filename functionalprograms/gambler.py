"""

Name    : Gambler.py
Date    : 26/08/2019
Purpose : Simulates a gambler who start with $stake and place fair $1 bets until he/she goes broke (i.e. has no money) or reach $goal

"""

from Utility import utility

while True:
    try:
        # recieving the stake and goal as inputs from the user
        stake=int(input("Enter your stake : "))
        goal=int(input("Enter your goal : "))
        # Calling the function in the BL file
        utility.gambler(stake, goal)
        break
    except ValueError:
        print("Please Enter numbers only")



