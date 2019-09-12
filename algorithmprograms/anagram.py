"""
Name    : Anagram.py
date    : 26/08/2019
Purpose : Take 2 Strings as Input such abcd and dcba and Check for Anagrams

"""


from Utility import utility

while True:
    #Getting the two strings from the user
    try:
        s1=input("Enter the first string : ")
        s2 =input("Enter the second string : ")
        if (s1.isspace() or s2.isspace()):
            print("White space is not allowed as input.. Try once more ; ")
            continue
        if(s1.isdigit() != True and s2.isdigit() != True):
            break
        else:
            print("Enter words only")
    except ValueError:
        print("Enter words only")

#Calling the function in the BL file
utility.checkanagram(s1,s2)
