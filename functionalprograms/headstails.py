"""

Name    : HeadsTails.py
Date    : 26/08/2019
Purpose : Flip Coin and print percentage of Heads and Tails

"""


from Utility import utility

#Getting the number of times the user wants to flip the coin
n = int(input("Enter the number of times you want to Flip the coin : "))

#Checking whether the number is positive or not
if n < 1:
    print("Invalid Input..Enter a Positive Number : ")
else:
    utility.headstails(n)
