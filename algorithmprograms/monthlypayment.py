"""

Name    : MonthlyPayment
Date    : 26/08/2019
Purpose : reads in three command-line arguments P, Y, and R
          and calculates the monthly payments you would have to make

"""

from Utility import utility

while True:
    #Getting the inputs from the user
    try:
        principle=int(input("Enter the principal amount :"))
        if(principle < 1):
            print("Amount should be positive integers")
            continue
        break
    except ValueError:
        print("Enter amount in numbers only")
        continue

while True:
    try:
        year=int(input("Enter the number of years : "))
        if(year < 1):
            print("The number of years should be positive integers only")
            continue
        break
    except ValueError:
        print("Enter number of years in numbers only")
        continue
while True:
    try:
        rate=int(input("Enter the rate of interest : "))
        if(rate < 1):
            print("Rate of interst must be a positive integer")
            continue
        break
    except ValueError:
        print("Enter the interest in integers only")
        continue

#calling the function in the BL file
payment=utility.monthlypayment(principle,year,rate)

#Printing the monthly payment
print("Monthly Payment : ",payment)