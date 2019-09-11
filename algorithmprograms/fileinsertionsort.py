"""

Name     : FileInsertionSort
Date     : 26/08/2019
Purpose  : Reads in string from a file and prints them in sorted order, write that to the same file

"""

from Utility import utility
import sys

try:
    #write the contents into the file
    f1=open("abc.txt","w+")
except FileNotFoundError as e:
    print(e)
    sys.exit()

f1.write("jettus thanzeeh janis sreeraj abhi noothan")
f1.close()

try:
    #Read the contents from the file
    with open('abc.txt') as f:
        content = f.read().split(' ')
except FileNotFoundError as e:
    print(e)
    sys.exit()


#Printing the contents before srting
print("Before Sorting : " ,content)

#Calling the function in the BL file
list2=utility.fileinsertionsort(content)

#Printing the contents After Sorting
print("After Sorting : ",list2)

try:
    #Writing the sorted list into the file
    with open('abc.txt', 'w') as f3:
        for contents in list2:
            f3.write('%s\n' % contents)
except FileNotFoundError as e:
    print(e)
    sys.exit()