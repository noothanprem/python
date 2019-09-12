"""

Name    : IntegerBubbleSort
Date    : 26/08/2019
Purpose : BubbleSort for Integers

"""


from Utility import utility
import sys

while True:
    try:
        #Get the total number of elements that the user is going to enter
        n=int(input("Enter the number of elements : "))
        if(n < 1):
            print("Enter Positive integers only")
            continue
        break
    except ValueError:
        print("Enter numbers only")

list1=[]

#putting the elements into the list
print("Enter the elements : ")
for i in range(0,n):
    try:
        d=int(input())
    except ValueError:
        print("Enter numbers only")
        sys.exit()
    list1.append(d)

#Prints the elemments of the list before sorting
print("Before Sorting : ",list1)

#calls the function in the BL file
list2=utility.intbubble(n,list1)

#Printing the list after sorting :
print("After Sorting : ",list2)