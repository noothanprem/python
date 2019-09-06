"""
Name    : Anagram.py
date    : 26/08/2019
Purpose : Take 2 Strings as Input such abcd and dcba and Check for Anagrams

"""


from Utility import utility

#Getting the two strings from the user
s1=input("Enter the first string : ")
s2 =input("Enter the second string : ")

#Calling the function in the BL file
utility.checkanagram(s1,s2)
