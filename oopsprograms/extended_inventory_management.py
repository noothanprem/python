"""

    Name : extended_inventory_management.py
    Date : 31/08/2019
    Purpose : To extend the above program.The InventoryManager will call each Inventory Object in its list
                to calculate the Inventory Price

"""


from oopsprograms.extendedinventorymanagement_utility import Exinvent

#creates the object of the class
ex=Exinvent()
#calling the function to open the file and storing the contents
dict1=ex.file_open()
print(dict1)
bool1=1
while(bool1 == 1):
    #Displaying the items available for the user to choose
    print("1.rice")
    print("2.pulses")
    print("3.wheats")
    category=input("Enter what you want : ")
    print("Select from the following types : ")
    for i in range(3):
        #Displays the categories available in the selected item
        print(i+1,". ",dict1[category][i]["name"])
    #Storing the selected category
    rtype=int(input("Enter the option : "))
    #Searching for the category by calling the function
    ex.search(dict1,rtype,category)
    bool1=int(input("Enter 1 to continue or 2 to exit : "))

    

    
