"""

Name     : FileBubbleSort.py
Date     : 26/08/2019
Purpose  : Reads in integers from a file ,prints them in sorted order using Bubble Sort and write that to the same file


"""




from Utility import utility

#Writing contents to into the file
f1=open("xyz.txt","w+")
f1.write("jettus thanzeeh janis sreeraj abhi noothan")
f1.close()

#Reading the contents from the file
f2=open("abc.txt","r")
with open('xyz.txt') as f:
    content = f.read().split(' ')
f2.close()

#Printing the contents
print("Before Sorting : " ,content)

#Calling the function in the BL file
list2=utility.bubsort(content)

print("After Sorting : ",list2)

#Writing the sorted content into the file
with open('xyz.txt', 'w') as f3:
    for contents in list2:
        f3.write('%s\n' % contents)
