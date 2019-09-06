"""

Name     : FileInsertionSort
Date     : 26/08/2019
Purpose  : Reads in string from a file and prints them in sorted order, write that to the same file

"""

from Utility import utility

#write the contents into the file
f1=open("abc.txt","w+")
f1.write("jettus thanzeeh janis sreeraj abhi noothan")
f1.close()

#Read the contents from the file
f2=open("abc.txt","r")
with open('abc.txt') as f:
    content = f.read().split(' ')
f2.close()

#Printing the contents before srting
print("Before Sorting : " ,content)

#Calling the function in the BL file
list2=utility.insertionsort(content)

#Printing the contents After Sorting
print("After Sorting : ",list2)

#Writing the sorted list into the file
with open('abc.txt', 'w') as f3:
    for contents in list2:
        f3.write('%s\n' % contents)