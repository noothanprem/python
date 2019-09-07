"""

    Name : linkedlist_shares.py
    Date : 31/08/2019
    Purpose : To Maintain the List of CompanyShares in a Linked List So new CompanyShares can
              be added or removed easily.

"""


from oopsprograms import linkedlistsharesutility

#Creating the object for the Linked List class
list1=linkedlistsharesutility.LinkedList()
#Creating the object for the Jsoninteract class
j1=linkedlistsharesutility.Jsoninteract()
#calling the function to open the json file and reading the data in the file
json_string=j1.file_open()

#Iterates through all the lements in the string
for i in json_string:
    print(i)
    #Adding each element of the string to the LinkedList by calling add() method
    list1.add(i)

c=1
while(c == 1):
    print("1.Display")
    print("2.Add Share")
    print("3.Remove Share")
    op=int(input("Enter 1,2, or 3 : "))
    #Calls the display() method of LinkedList if the user choosed 1
    if(op == 1):
        list1.display()
    # Calls the add() method for adding new shares if user has selected 2
    elif(op == 2):
        #calling add() method of the file and stores the string
        json_string=j1.add(json_string)
        list1.add(json_string)
        #calls the update() to update the new json_string into the file
        j1.file_update(json_string)
    elif(op == 3):
        # calling remove() method of the LinkedList if the user has choosed 3
        list1.remove()
    c=int(input("Enter 1 to continue and 2 to exit : "))
        

