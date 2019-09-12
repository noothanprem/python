"""

    Name    : orderedlist.py
    Date    : 31/08/2019
    Purpose : To read a List of Numbers from a file and arrange it ascending Order in a
              Linked List. Take user input for a number, if found then pop the number out of the
              list else insert the number in appropriate position

"""

from datastructureprograms.orderedlist_utility import LinkedList


#creating an object of LinkedList class
my_list=LinkedList()

#opening the file with only 'read' permission
try:
    with open('abc.txt') as f:
        content = f.read().split(',')
except FileNotFoundError as e:
    print(e)
#printing the contents of the file
print(content)

i=0
#Iterates the loop till 'i' reaches the length of 'content'
while i < len(content):
    #Adding each element to the linked list by calling add() method
    my_list.add(int(content[i]))
    i += 1

#Displaying the Linkedlist contents
my_list.display()

while True:
    try:
        #Asks for the number to search from the user
        s1 = int(input("Enter the number which you want to search : "))
        break
    except ValueError:
        print("Only numbers are allowed")
        continue

#calling the search() method of LinkedList
my_list.search(s1)

try:
    #Opening the other file foe writing updated data
    with open("xyz.txt","w+") as f3:
        #Iterates till we reach the last element of the linked list
        while my_list.size() > 0:
            #calling da() functionj of the LinkedList
            print(my_list.da())
            #writing the element to the file
            f3.write(str(my_list.da()))
            #Giving a space after the element
            f3.write(" ")
            #removes that element from the list by calling the remove() method
            my_list.remove(0)
except FileNotFoundError as e:
    print(e)