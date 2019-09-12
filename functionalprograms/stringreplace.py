"""

Name    : stringreplace.py
Date    : 26/08/2019
Purpose : Take user Input and Replace String Template “Hello <<UserName>>, How are you?”

"""


from Utility import utility
import sys


while True:

    #Getting the full string from the user
    s1=input("Enter the string : ")
    if(s1.isdigit()):
        print("Numbers are not allowed")
        continue
    if(s1.isspace()):
        print("White spaces are not allowed")
        continue
    specialChars = ["$", "#", "@", "!", "*", "+", "-", ",", "%", "^", "(", ")", "[", "]", "{", "}", ":", ";",
                    "'", "<",
                    ">", "?", "~"]
    for i in s1:
        for j in specialChars:
            if (i == j):
                print("No Special characters allowed.. Please try once more")
                sys.exit()

    #Getting the new word to replace
    s2=input("Enter the string which you want to replace with : ")
    if (s2.isdigit()):
        print("Numbers are not allowed")
        continue
    if (s2.isspace()):
        print("White spaces are not allowed")
        continue
    specialChars = ["$", "#", "@", "!", "*", "+", "-", ",", "%", "^", "(", ")", "[", "]", "{", "}", ":", ";",
                    "'", "<",
                    ">", "?", "~"]
    for i in s2:
        for j in specialChars:
            if (i == j):
                print("No Special characters allowed.. Please try once more")
                sys.exit()
    break
#calling the function in the BL file
string3=utility.strreplace(s1,s2)
print("New String : ", string3)

