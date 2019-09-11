"""

Name    : DayOfWeek.py
Date    : 26/08/2019
Purpose : Take a date as input and print the day of the week that date falls on.

"""


from Utility import utility

#Getting the month,date and year from the user
while True:
    try:
        month=int(input("Enter the month : 1 for january,2 for february,..etc"))
        date=int(input("Enter the date : "))
        year=int(input("Enter the year : "))
        break
    except ValueError:
        print("Enter everything as numbers only")

#Calling the function in the BL file
d=utility.date(month,date,year)
print(d)