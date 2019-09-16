"""

    Name    : unorderedlist.py
    Date    : 31/08/2019
    Purpose : To Read the Text from a file, split it into words and arrange it as Linked List.
              Take a user input to search a Word in the List. If the Word is not found then add it
              to the list, and if it found then remove the word from the List.

"""


from datastructureprograms.unorderedlist_utility import LinkedList
import sys


#creates an object for LinkedList class
my_list=LinkedList()

try:
    #Opens the file for reading
    with open('abc.txt') as f:
        content = f.read().split(',')
except FileNotFoundError as e:
    print(e)
    sys.exit()

#prints the contents of the       file
print(content)


i=0
#Adding each element to the Linked List by calling 'add()' method
while i < len(content):
    my_list.add(content[i])
    i+=1




#Displaying the contents of the Linked List
my_list.display()

s1=''
while True:
    #prompts the user to enter the number which he wants to search
    s1=input("Enter the number which you want to search : ")
    if(s1.isdigit() == False):
        print("Please enter integer numbers only")
        continue
    specialChars = ["$", "#", "@", "!", "*", "+", "-", ",", "%", "^", "(", ")", "[", "]", "{", "}", ":", ";", "'", "<",
                    ">", "?", "~"]
    for i in s1:
        for j in specialChars:
            if (i == j):
                print("No Special characters allowed.. Please try once more")
                sys.exit()
    break

#calling the 'search()' method of Linked List
my_list.search(s1)


try:
    #Open the file for writing it back to the file
    with open("xyz.txt","w+") as f3:
        # for item in my_list:
            # f3.write('%s\n' % item)
        #Loop iterates till the LinkedList becomes empty
        while my_list.size() > 0:
            #calls the da() method to get the head node in each iteration
            print(my_list.da())
            #writing the data to the file in each iteration
            f3.write(str(my_list.da()))
            f3.write(" ")
            #removes the head element from the linked list in each iteration
            my_list.remove(0)
except FileNotFoundError as e:
    print(e)