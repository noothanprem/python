"""

    Name : stock_stack.py
    Date : 31/08/2019
    Purpose : Further maintain the Stock Symbol Purchased or Sold in a Stack implemented using
                Linked List to indicate transactions done.

"""

from oopsprograms.stockstack_utility import Stack
import json
import datetime
import sys

#Function to display the stock
def displaystock(json_string):
    #Loop iterates equal to the length of the json_string
    for i in range(len(json_string)):
        #Accesses the fields of each and prints it
        print("Name of the company : ",json_string[i]['name'])
        print("Share Count : ",json_string[i]['share_count'])
        print("Share Cost : ",json_string[i]['share_price'])
#creates a dictionary
dict1={
    "name":None,
    "share_count":None,
    "share_price":None,
    "update_date":None
}

#Function to perform buy operation
def buystock(json_string):
    # Takes the company name as the input
    c_name = ''
    while True:
        c_name = input("Enter the company name : ")
        if (c_name.isdigit()):
            print("Numbers are not allowed")
            continue
        if (c_name.isspace()):
            print("White spaces are not allowed")
            continue
        specialChars = ["$", "#", "@", "!", "*", "+", "-", ",", "%", "^", "(", ")", "[", "]", "{", "}", ":", ";",
                        "'", "<",
                        ">", "?", "~"]
        for i in c_name:
            for j in specialChars:
                if (i == j):
                    print("No Special characters allowed.. Please try once more")
                    sys.exit()
        break
    #Loop iterates equal to the length of the string
    for i in range(len(json_string)):
        #Checks whether the name is same as the given name in each iteration
        if(json_string[i]["name"] == c_name):
            #If the name is found, then update the share_count and other details according to the user's input
            share = 0
            price = 0
            while True:
                try:
                    share = int(input("Enter the number of shares : "))
                    if (share < 1):
                        print("Share count should be a positive integer")
                        continue
                except ValueError:
                    print("Share count should be a number")
                    continue
                break

            while True:
                try:
                    price = int(input("Enter the Share price : "))
                    if (price < 1):
                        print("Price should be a positive integer")
                        continue
                except ValueError:
                    print("Price should be  should be an integer")
                    continue
                break
            json_string[i]['share_count']=int(json_string[i]['share_count'])+share
            json_string[i]['share_price']=price
            json_string[i]['update_date']=str(datetime.datetime.now())
            #Push the updated part of the string to the stack
            s1.push(json_string[i])
            return json_string

    #If the given company is not available, then store all the information in a dictionary
    dict1["name"]=c_name
    share = 0
    price = 0
    while True:
        try:
            share = int(input("Enter the number of shares : "))
            if (share < 1):
                print("Share count should be a positive integer")
                continue
        except ValueError:
            print("Share count should be a number")
            continue
        break

    while True:
        try:
            price = int(input("Enter the Share price : "))
            if (price < 1):
                print("Price should be a positive integer")
                continue
        except ValueError:
            print("Price should be  should be an integer")
            continue
        break
    dict1["share_count"]=share
    dict1["share_price"]=price
    dict1["update_date"]=str(datetime.datetime.now())
    #Append the dictionary to the json_string
    json_string.append(dict1)
    return json_string

#Function to sell the stock
def sellstock(json_string):
    # Takes the company name as the input
    c_name = ''
    while True:
        c_name = input("Enter the company name : ")
        if (c_name.isdigit()):
            print("Numbers are not allowed")
            continue
        if (c_name.isspace()):
            print("White spaces are not allowed")
            continue
        specialChars = ["$", "#", "@", "!", "*", "+", "-", ",", "%", "^", "(", ")", "[", "]", "{", "}", ":", ";",
                        "'", "<",
                        ">", "?", "~"]
        for i in c_name:
            for j in specialChars:
                if (i == j):
                    print("No Special characters allowed.. Please try once more")
                    sys.exit()
        break

    #Iterates through all the elements in the json string
    for i in range(len(json_string)):
        #Checks whether the given company is available or not
        if(json_string[i]['name'] == c_name):
            #If it is available, get the share_count they want to sell
            while True:
                try:
                    share = int(input("Enter the number of shares : "))
                    if (share < 1):
                        print("Share count should be a positive integer")
                        continue
                except ValueError:
                    print("Share count should be a number")
                    continue
                break
            #Check whether that much share_count is available or not
            if(int(json_string[i]['share_count']) < share):
                #If not available, prompt the user
                print("Insufficient shares")
                return
            else:
                #If available, update the share_count and share_date
                json_string[i]['share_count']=int(json_string[i]['share_count']) - share
                json_string[i]['update_date']=str(datetime.datetime.now())
                #Push the updated data into the stack
                s1.push(json_string[i])
                return json_string
    #If it comes out of the loop, that means, the company is not available
    print("The given company is not available")


#Function to open the json file
def file_open():
    try:
        #Opens the file with read permission
        with open("stock.json","r",encoding='utf-8') as f:
            content=f.read()
 
        json_string=json.loads(content)
        return json_string
    except FileNotFoundError as e:
        print(e)


#Function to update the json file
def file_update(json_string):
    try:
        #Opens the file with write permission
        with open("stock.json","w") as f:
            json.dump(json_string,f)
        return True
    except FileNotFoundError as e:
        print(e)    

if __name__ == "__main__":

    #calling the file_open() fucation and reading the data
    json_string =file_open()

    #creating object of the Stack class
    s1=Stack()

    while True:
        print("1.Display")
        print("2.Buy")
        print("3.Sell")
        print("4.Print the completed transactions")
        while True:
            try:
                n=int(input("Select an option : "))
                if(n < 1 or n > 4):
                    print("Enter 1,2,3, or 4")
                    continue
                break
            except ValueError:
                print("Enter 1,2,3,or 4")
                continue
        #call displaystock() if the user has selected '1'
        if(n == 1):
            displaystock(json_string)
        elif(n == 2):
            # call buystock() if the user has selected '2'
            json_string=buystock(json_string)
            #calling file_update function to update data in the file
            file_update(json_string)
        elif(n == 3):
            # call buystock() if the user has selected '3'
            json_string=sellstock(json_string)
            #calls file_update() to update the data in the file
            file_update(json_string)
        elif(n == 4):
            len1=len(json_string)
            print("Completed Transactions : ")
            print()
            #Loop iterates equl to the length of the json_string
            for i in range(len1):
                if(s1.isempty() != True):
                    #popping out each element from the stack and printing it
                    ele=s1.pop()
                    print(ele)
        c=int(input("Do you want to continue(1) or exit(2)"))
        if(c == 2):
            break
            

        
    
