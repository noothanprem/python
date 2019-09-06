"""

Name    : stringreplace.py
Date    : 26/08/2019
Purpose : Take user Input and Replace String Template “Hello <<UserName>>, How are you?”

"""


from Utility import utility

#Getting the full string from the user
s1=input("Enter the string : ")
#Getting the new word to replace
s2=input("Enter the string which you want to replace with : ")

#calling the function in the BL file
string3=utility.strreplace(s1,s2)
print("New String : ", string3)

