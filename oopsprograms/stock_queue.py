"""

    Name : stock_queue.py
    Date : 31/08/2019
    Purpose : To extend the above program to maintain DateTime of the transaction in a Queue implemented using Linked
              List to indicate when the transactions were done.

"""


from oopsprograms.stockqueue_utility import Queue
import datetime
import json

#Function to display stock
def displaystock(json_string):
    print(json_string)
    #Loop continues until it reaches the length of the string
    for i in range(len(json_string)):
        #Prints the details about shares in each company
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
    #Takes the company name as the input
    c_name=input("Enter the company name : ")
    #Used to iterate through the json_string
    for i in range(len(json_string)):
        #checks whether this is the company we are searching for or not
        if(json_string[i]["name"] == c_name):
            #If the comppany is found, then update all the details by taking the inputs from the user
            json_string[i]['share_count']=int(json_string[i]['share_count'])+int(input("Enter the number of shares : "))
            json_string[i]['share_price']=int(input("Enter the share cost : "))
            json_string[i]['update_date']=str(datetime.datetime.now())
            #adding the updated jsonstring to the queue
            q1.enqueue(json_string[i])
            return json_string
     #Storing the details into a dictionary if the given company does not exist
    dict1["name"]=c_name
    dict1["share_count"]=int(input("Enter the number of shares"))
    dict1["share_price"]=int(input("Enter the share price"))
    dict1["update_date"]=str(datetime.datetime.now())
    #Appending the dictionary to the json string
    json_string.append(dict1)
    return json_string

#Function to sell the stock
def sellstock(json_string):
    #Gets the company name from the user
    c_name=input("Enter the company name : ")
    #Iterates through the json_string
    for i in range(len(json_string)):
        #Looks for the company name in the json_string
        if(json_string[i]['name'] == c_name):
            #If it matches, then get the number of shares
            s_count=int(input("Enter the number of shares"))
            #Checks whether the given share count is greater than the share count or not
            if(int(json_string[i]['share_count']) < s_count):
                #If it is not enough, print insufficient funds
                print("Insufficient shares")
                return
            else:
                #decrements the share_count
                json_string[i]['share_count']=int(json_string[i]['share_count']) - s_count
                json_string[i]['update_date']=str(datetime.datetime.now())
                #Enters the data into the queue
                q1.enqueue(json_string[i])
                return json_string
    print("The given company is not available")


#Function to open the json file
def file_open():
    try:
        #Opens the json file with 'read' permission
        with open("stock.json","r",encoding='utf-8') as f:
            content=f.read()

        json_string=json.loads(content)
        return json_string
    except FileNotFoundError as e:
        print(e)

#Function to open the file for updating the data
def file_update(json_string):
    try:
        with open("stock.json","w") as f:
            json.dump(json_string,f)
        return True
    except FileNotFoundError as e:
        print(e)    

if __name__ == "__main__":

    #calls the file_open() functio to open the file and stores the contents
    json_string =file_open()
    #creates an object of Queue
    q1=Queue()
    bool1="True"
    while(bool1 == "True"):
        print("1.Display")
        print("2.Buy")
        print("3.Sell")
        print("4.Print the completed transactions")
        n=int(input("Select an option : "))
        #calls the display() method if user has selected '1'
        if(n == 1):
            displaystock(json_string)
        elif(n == 2):
            # calls the buystock() method and stores the json_string if user has selected '2'
            json_string=buystock(json_string)
            #Calls the file_update() method to update the json_string in the file
            file_update(json_string)
        elif(n == 3):
            # calls the sellstock() method and stores the json_string if user has selected '3'
            json_string=sellstock(json_string)
            # Calls the file_update() method to update the json_string in the file
            file_update(json_string)
        elif(n == 4):
            #takes the length of the json_string
            len1=len(json_string)
            print("Completed Transactions : ")
            #Loop continues until the queue becomes empty
            while(q1.isEmpty() != True):
                #removes each element and stores
                ele=q1.dequeue()
                #displays each element
                print(ele)