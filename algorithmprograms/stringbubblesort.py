"""

Name     : stringbubblesort.py
Date     : 26/08/2019
Purpose  : BubbleSort for String

"""


from Utility import utility
import sys


while True:
    try:
        #Getting the number of elements that the user wants to enter
        n=int(input("Enter the number of elements : "))
        if(n < 1):
            print("Enter Positive integers only")
            continue
        break
    except ValueError:
        print("Enter in integers only")
        continue

list1=[]

#putting the elements into a list
print("Enter the elements : ")
for i in range(0,n):
    word=input()
    if(word.isdigit()):
        print("Numbers are not allowed")
        sys.exit()
    if(word.isspace()):
        print("White spaces are not allowed")
    specialChars = ["$", "#", "@", "!", "*", "+", "-", ",", "%", "^", "(", ")", "[", "]", "{", "}", ":", ";", "'", "<",
                    ">", "?", "~"]
    for i in word:
        for j in specialChars:
            if (i == j):
                print("No Special characters allowed.. Please try once more")
                sys.exit()
    list1.append(word)

#Printing the elements before sorting
print("Before Sorting : ",list1)

#Calling the function in the BL file
list2=utility.strbubblesort(n,list1)

#Printing the sorted list
print("Sorted List : ",list2)