"""

Name    : IntegerBinarySearch.py
Date    : 26/08/2019
Purpose : BinarySearch  for integers

"""

from Utility import utility
import sys

n=0
while True:
    try:
        #getting the number of elements that the user is going to give
        n=int(input("Enter the number of elements you need "))
        if(n > 0):
            break
        else:
            print("Enter Positive integers only")
            continue
    except ValueError:
        print("Please enter number only")
        continue

#writing those elements into a list
print("Enter the elements : ")
list1=[]
for i in range(0,n):
    try:
        d=int(input())
    except ValueError:
        print("Please enter integers only")
        sys.exit()
    list1.append(int(d))



while True:
    try:
        # Getting the element which the user wants to search
        print("Enter the element which you want to search : ")
        elem=int(input())
        break
    except ValueError:
        print("Please enter numbers only")

#calling the function in the BL file
utility.binarysearch(n,list1,elem)