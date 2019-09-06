"""

Name    : IntegerInsertion.py
Date    : 26/08/2019
Purpose : insertionSort method for integers

"""


from Utility import utility

#Getting the total number of elements that the user is going to enter
n=int(input("Enter the number of elements : "))

print("Enter the elements : ")
list1=[]
#Storing the elements into a list
for i in range(0,n):
    list1.append(int(input()))

#Calling the function in the BL file
list2=utility.integerinsertion(n,list1)

#printing the list After sorting
print("After Sorting : ",list2)