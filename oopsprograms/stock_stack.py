from oopsprograms.stockstack_utility import Stack
import json
import datetime


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
    #Takes the company name
    c_name=input("Enter the company name : ")
    #Loop iterates equal to the length of the string
    for i in range(len(json_string)):
        #Checks whether the name is same as the given name in each iteration
        if(json_string[i]["name"] == c_name):
            #If the name is found, then update the share_count and other details according to the user's input
            json_string[i]['share_count']+=int(input("Enter the number of shares : "))
            json_string[i]['share_price']=int(input("Enter the share cost : "))
            json_string[i]['update_date']=str(datetime.datetime.now())
            #Push the updated part of the string to the stack
            s1.push(json_string[i])
            return json_string

    #If the given company is not available, then store all the information in a dictionary
    dict1["name"]=c_name
    dict1["share_count"]=int(input("Enter the number of shares"))
    dict1["share_price"]=int(input("Enter the share price"))
    dict1["update_date"]=str(datetime.datetime.now())
    #Append the dictionary to the json_string
    json_string.append(dict1)
    return json_string

#Function to sell the stock
def sellstock(json_string):
    #Takes the company name from the user
    c_name=input("Enter the company name : ")
    #Iterates through all the elements in the json string
    for i in range(len(json_string)):
        #Checks whether the given company is available or not
        if(json_string[i]['name'] == c_name):
            #If it is available, get the share_count they want to sell
            s_count=int(input("Enter the number of shares"))
            #Check whether that much share_count is available or not
            if(int(json_string[i]['share_count']) < s_count):
                #If not available, prompt the user
                print("Insufficient shares")
                return
            else:
                #If available, update the share_count and share_date
                json_string[i]['share_count']=int(json_string[i]['share_count']) - s_count
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
    bool1="True"
    while(bool1 == "True"):
        print("1.Display")
        print("2.Buy")
        print("3.Sell")
        print("4.Print the completed transactions")
        n=int(input("Select an option : "))
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
            

        
    
