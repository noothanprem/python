"""

Name    : StringBinarySearch.py
Date    : 26/08/2019
Purpose : BinarySearch for String

"""


from Utility import utility
import sys

while True:
    try:
        #getting the number of elements that the user wants to enter
        n=int(input("Enter the number of elements you need "))
        if(n < 1):
            print("Enter Positive integers only")
            continue
        break
    except ValueError:
        print("Enter number of elements as integers only")
        continue

print("Enter the elements : ")
list1=[]
#putting the elements into a list
for i in range(0,n):
    d=input()
    if(d.isdigit()):
        print("Numbers are not allowed")
        sys.exit()
    if(d.isspace()):
        print("White spaces are not allowed")
        sys.exit()
    specialChars = ["$", "#", "@", "!", "*", "+", "-", ",", "%", "^", "(", ")", "[", "]", "{", "}", ":", ";", "'", "<",
                    ">", "?", "~"]
    for i in d:
        for j in specialChars:
            if (i == j):
                print("No Special characters allowed.. Please try once more")
                sys.exit()
    list1.append(d)

while True:
    #Getting the element which the user want to search
    print("Enter the element which you want to search : ")
    elem=input()
    if(elem.isdigit()):
        print("Numbers are not allowed")
        continue
    if(elem.isspace()):
        print("White spaces are not allowed")
        continue
    specialChars = ["$", "#", "@", "!", "*", "+", "-", ",", "%", "^", "(", ")", "[", "]", "{", "}", ":", ";", "'", "<",
                    ">", "?", "~"]
    for i in elem:
        for j in specialChars:
            if (i == j):
                print("No Special characters allowed.. Please try once more")
                sys.exit()
    break

#calling the function in the BL file
utility.stringbinary(n,list1,elem)