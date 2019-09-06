"""

Name     : stringbubblesort.py
Date     : 26/08/2019
Purpose  : BubbleSort for String

"""


from Utility import utility

#Getting the number of elements thst the user wants to enter
n=int(input("Enter the number of elements : "))

list1=[]

#putting the elements into a list
print("Enter the elements : ")
for i in range(0,n):
    list1.append(input())

#Printing the elements before sorting
print("Before Sorting : ",list1)

#Calling the function in the BL file
list2=utility.strbubblesort(n,list1)

#Printing the sorted list
print("Sorted List : ",list2)