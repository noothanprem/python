import json
import datetime

class Commercial:

    #Function to open the file for reading the data
    def file_open(self):
        #Opens the file with 'read' permission
        with open("commercial.json", "r") as f:
            content = f.read()
        #Decode the json string and stores it as a string
        json_string = json.loads(content)
        #returns the string
        return json_string

    #Function to update the file
    def file_update(self, json_string):
        #opens the file with write permission
        with open("commercial.json", "w") as f:
            json.dump(json_string, f) #writes the string into the file

    #Function to display
    def display(self, json_string):
        print(json_string)
        i = 0
        #Loop iterates until 'i' reaches the length of the json string
        while (i < len(json_string)):
            print("Name of the company : ", json_string[i]["name"])
            print("Number of shares : ", json_string[i]["share_count"])
            print("Share Price : ", json_string[i]["share_price"])
            i += 1

    #Function to find the value
    def findvalue(self, json_string):
        #Takes the company name from the user
        c_name = input("Enter the company name : ")
        #finds the length
        len1 = len(json_string)
        #Loop iterates until it reaches the length of the json string
        for i in range(len1):
            #Checks whether the name of the element is same as the given name in each iteration
            if (json_string[i]["name"] == c_name):
                #calculates the value
                print("value = ", int(json_string[i]["share_count"]) * int(json_string[i]["share_price"]))
                return
        #if it completes the loop and comes out, then that company won't be there in that list
        print("The Given company is not available")


    #function to perfor buy operation
    def buy(self, json_string):
        #takes the company name from the user
        c_name = input("Enter the company name : ")
        #finds the length of the json string
        len1 = len(json_string)
        #creates a dictionary for storing the company details if it is a new company
        dict1 = {
            "name": None,
            "share_count": None,
            "share_price": None,
            "update_time": None
        }
        #Loop iterates through all the elements in the string
        for i in range(len1):
            #checks whether the given company nname is same as the currennt company name or not in each iteration
            if (c_name == json_string[i]["name"]):
                #Asks the share count and adds it with the current share count
                json_string[i]["share_count"] = int(json_string[i]["share_count"]) + int(input("Enter the number of shares : "))
                #asks the share price and changes the share price
                json_string[i]["share_price"] = input("Enter the share price : ")
                #takes the current time as updated time
                json_string[i]["updated_time"] = str(datetime.datetime.now())
                #returns the json string
                return json_string

        """if the name is not there in the string, then we will store then we will store the name and other details in a dictionar.
        And at last, we will append this dictionary to a string"""
        #Storing the name in the dictionary
        dict1["name"] = c_name
        #TAkes the share count and share price and stores it into the dictionary
        dict1["share_count"] = input("Enter the number of shares : ")
        dict1["share_price"] = input("Enter the share price : ")
        #Appends the dictionary to json string
        json_string.append(dict1)
        #returns the json string
        return json_string

    #Function to perform the sell operation
    def sell(self, json_string):
        #Takes the company name as the input
        c_name = input("Enter the company name : ")
        #Finds the length of the json string
        len1 = len(json_string)
        #Loop iterates through all the elements of the json string
        for i in range(len1):
            #Checks whether the company name is same or not in each iteration
            if (c_name == json_string[i]["name"]):
                #takes the number of shares as input
                shares = int(input("Enter the number of shares : "))
                #Checks whether the needed share is available or not
                if (shares > int(json_string[i]["share_count"])):
                    #If the shares are less, then print the message
                    print("Only ", json_string[i]["share_count"], " shares left, Please Re enter")
                    return json_string
                #If needed number of shares are available, then decrement the share count
                json_string[i]["share_count"] = int(json_string[i]["share_count"]) - shares
                return json_string
        print("The Given company is not available")