"""

Name    : SumOfThree.py
Date    : 26/08/2019
Purpose : Read in N integers and counts the   number of triples that sum to exactly 0.

"""

from Utility import utility

#Getting the total number of elements in the list
n=int(input("Enter the total number of elements : "))

#taking the elements from the user and storing into a list
list1=[]
print("Enter the elements :")
for i in range(0,n):
    elem=int(input())
    list1.append(elem)

#Printing the list
#print("The elements are : ")
#print(list1)

#Calling the function in the BL file
utility.sum(n,list1)