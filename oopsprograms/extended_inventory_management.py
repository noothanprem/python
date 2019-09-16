"""

    Name : extended_inventory_management.py
    Date : 31/08/2019
    Purpose : To extend the above program.The InventoryManager will call each Inventory Object in its list
                to calculate the Inventory Price

"""


from oopsprograms.extendedinventorymanagementmain import Exinvent

#creates the object of the class
ex=Exinvent()
#calling the function to open the file and storing the contents
dict1=ex.file_open()
print(dict1)

category=''
while True:
    #Displaying the items available for the user to choose
    while True:
        print("rice")
        print("pulses")
        print("wheats")
        category=input("Enter what you want : ")
        catlist=["rice","pulses","wheats"]
        if category not in catlist:
            print("Please enter any one of the three options")
            continue
        break
    print("Select from the following types : ")
    for i in range(3):
        #Displays the categories available in the selected item
        print(i+1,". ",dict1[category][i]["name"])
    rtype=0
    while True:
        try:
            #Storing the selected category
            rtype=int(input("Enter the option : "))
            if(rtype < 1 or rtype > 3):
                print("Enter either 1,2, or 3")
                continue
            break
        except ValueError:
            print("Enter either 1,2, or 3")
            continue
    #Searching for the category by calling the function
    ex.search(dict1,rtype,category)
    while True:
        c=int(input("Enter 1 to continue or 2 to exit : "))
        if(c != 1 and c != 2):
            print("Enter either 1 or 2")
            continue
        break
    if(c == 2):
        break

    

    
