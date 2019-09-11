"""

Name    : FileBinarySearch.py
Date    : 26/08/2019
Purpose : Read in a list of words from File. Then prompt the user to enter a word to search the list.
          The program reports if the search word is found in the list.

"""


from Utility import utility
import sys

while True:
    try:
         #Writing the contents to the file
        f1=open("abc.txt","w")
        break
    except FileNotFoundError:
        print("The file Does not exists")
        sys.exit()

f1.write("jettus thanzeeh janis sreeraj abhi noothan")
f1.close()

while True:
    try:
        #Reading the contents from the file
        with open('abc.txt') as f:
            content = f.read().split(' ')
            break
    except FileNotFoundError:
        print("The file Does not exists")
        sys.exit()






#Printing the file contents
print("Before Sorting : " ,content)

#Sorting the contents
content.sort()
print("After Sorting : ",content)

while True:
    #getting the wrd to be searched from the user
    s1=input("Enter the word to be searched : ")
    if(s1.isdigit() == True):
        print("Enter words only.. not digits")
    else:
        break


#calling the function in the BL file
utility.binary(content,s1)