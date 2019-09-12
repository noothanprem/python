"""

Name    : SumOfThree.py
Date    : 26/08/2019
Purpose : Read in N integers and counts the   number of triples that sum to exactly 0.

"""

from Utility import utility
import sys


#Getting the total number of elements in the list
while True:
    try:
        n=int(input("Enter the total number of elements : "))
        if(n < 1):
            print("Please enter a postive number, greater than 1")
            continue
        break
    except ValueError:
        print("Please enter a Positive number")
        continue
#taking the elements from the user and storing into a list
list1=[]
print("Enter the elements :")
for i in range(0,n):
    try:
        elem=int(input())
        list1.append(elem)
    except ValueError:
        print("Enter numbers only")
        sys.exit()



#Calling the function in the BL file
utility.sum(n,list1)
