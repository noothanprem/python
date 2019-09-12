"""

Name      : StringInsertionSort
Date      : 26/08/2019
Purpose   : insertionSort method for String

"""


from Utility import utility
import sys

while True:
    try:
        #Getting the total number of elements that the user is going to enter
        n=int(input("Enter the number of elements : "))
        if(n < 1):
            print("Enter positive integers only")
            continue
        break
    except ValueError:
        print("Enter integers only")
        continue

print("Enter the elements : ")
list1=[]
#Storing the elements into a list
for i in range(0,n):
    word=input()
    if(word.isdigit()):
        print("Numbers are not allowed")
        sys.exit()
    if(word.isspace()):
        print("Whitespaces are not allowed")
        sys.exit()

    specialChars = ["$", "#", "@", "!", "*", "+", "-", ",", "%", "^", "(", ")", "[", "]", "{", "}", ":", ";", "'", "<",
                    ">", "?", "~"]
    for i in word:
        for j in specialChars:
            if (i == j):
                print("No Special characters allowed.. Please try once more")
                sys.exit()
    list1.append(word)

#Calling the function in the BL file
list2=utility.stringinsertion(n,list1)

#printing the list After sorting
print("After Sorting : ",list2)