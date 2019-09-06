"""

Name    : IntegerBinarySearch.py
Date    : 26/08/2019
Purpose : BinarySearch  for integers

"""

from Utility import utility

#getting the number of elements that the user is going to give
n=int(input("Enter the number of elements you need "))
#writing those elements into a list
print("Enter the elements : ")
list1=[]
for i in range(0,n):
    list1.append(int(input()))

#Getting the element which the user wants to search
print("Enter the element which you want to search : ")
elem=int(input())

#calling the function in the BL file
utility.binarysearch(n,list1,elem)