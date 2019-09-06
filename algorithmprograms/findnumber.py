"""

Name    : FindNumber.py
Date    : 26/08/2019
Purpose : Takes a command-line argument N, asks you to think of a number between 0 and N-1, where N = 2^n,
          and always guesses the answer with n questions.

"""



from Utility import utility

#Getting the maximum limit for the number
n=int(input("Enter the limit : "))
print("Think of a Number b/w 0 and ",n-1)

#Calling the function in the BL file
utility.findnum(n)