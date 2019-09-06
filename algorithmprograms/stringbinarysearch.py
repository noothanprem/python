"""

Name    : StringBinarySearch.py
Date    : 26/08/2019
Purpose : BinarySearch for String

"""


from Utility import utility

#getting the number of elements that the user wants to enter
n=int(input("Enter the number of elements you need "))

print("Enter the elements : ")
list1=[]
#putting the elements into a list
for i in range(0,n):
    list1.append(input())

#Getting the element which the user want to search
print("Enter the element which you want to search : ")
elem=input()

#calling the function in the BL file
utility.stringbinary(n,list1,elem)