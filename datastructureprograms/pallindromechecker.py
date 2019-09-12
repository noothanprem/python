"""

    Name    : pallindromechecker.py
    Date    : 31/08/2019
    Purpose : To check whether a string is Pallindrome or not using dequeue

"""

from datastructureprograms.dequeue_utility import Dequeue
import sys

str1=''
while True:
    # Take the string as input
    str1 = input("Enter the string : ")
    if(str1.isdigit()):
        print("Numbers are not allowed")
        continue
    specialChars = ["$", "#", "@", "!", "*", "+", "-", ",", "%", "^", "(", ")", "[", "]", "{", "}", ":", ";", "'", "<",
                    ">", "?", "~"]
    for i in str1:
        for j in specialChars:
            if (i == j):
                print("No Special characters allowed.. Please try once more")
                sys.exit()
    break
# Setting the counter 'size' as '0'
size = 0

# Loop iterates till it reaches the end of the string
for i in str1:
    size += 1
# creating the object of the class by passing the length of the string
dequeue1 = Dequeue(size - 1)
# Iterates through each element of the string
for i in str1:
    # calls the addRear() method for adding each element
    dequeue1.addRear(i)
#Initializes the 'count' with '0'
count = 0
#creates two empty string
str2 = ""
c1 = ''

while count != (size):
    count += 1
    #removeRear() method removes and returns an element at each iteration
    c1 = dequeue1.removeRear(count)
    #Adds each each element to the string
    str2 += str(c1)
print(str2)

"""If the first string and the retrieved string are equal, it is a Pallindrome.
If those are not equal, not pallindrome"""
if (str1 == str2):
    print(str1, " is Pallindrome")
else:
    print(str1, "is not Pallindrome")
