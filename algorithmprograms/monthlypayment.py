"""

Name    : MonthlyPayment
Date    : 26/08/2019
Purpose : reads in three command-line arguments P, Y, and R
          and calculates the monthly payments you would have to make

"""

from Utility import utility

#Getting the inputs from the user
principle=int(input("Enter the principal amount :"))
year=int(input("Eter the number of years : "))
rate=int(input("Enter the rate of interest : "))

#calling the function in the BL file
payment=utility.monthlypayment(principle,year,rate)

#Printing the monthly payment
print("Monthly Payment : ",payment)