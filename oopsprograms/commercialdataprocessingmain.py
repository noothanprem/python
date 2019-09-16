import json
import datetime
import sys

class Commercial:

    #Function to open the file for reading the data
    def file_open(self):

        try:
            #Opens the file with 'read' permission
            with open("commercial.json", "r") as f:
                content = f.read()
            #Decode the json string and stores it as a string
            json_string = json.loads(content)
        except FileNotFoundError as e:
            print(e)
            sys.exit()

        #returns the string
        return json_string


    #Function to update the file
    def file_update(self, json_string):

        try:
            #opens the file with write permission
            with open("commercial.json", "w") as f:
                json.dump(json_string, f) #writes the string into the file
        except FileNotFoundError as e:
            print(e)


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
        c_name=''
        while True:
            c_name = input("Enter the company name : ")
            if(c_name.isdigit()):
                print("Numbers are not allowed")
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
        c_name=''
        while True:
            c_name = input("Enter the company name : ")
            if (c_name.isdigit()):
                print("Numbers are not allowed")
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
                share=0
                price=0
                while True:
                    try:
                        share=int(input("Enter the number of shares : "))
                        if(share < 1):
                            print("Share count should be a positive integer")
                            continue
                    except ValueError:
                        print("Share count should be a number")
                        continue
                    break

                while True:
                    try:
                        price=int(input("Enter the Share price : "))
                        if(price < 1):
                            print("Price should be a positive integer")
                            continue
                    except ValueError:
                        print("Price should be  should be an integer")
                        continue
                    break

                json_string[i]["share_count"] = int(json_string[i]["share_count"]) + share
                #asks the share price and changes the share price
                json_string[i]["share_price"] = price
                #takes the current time as updated time
                json_string[i]["updated_time"] = str(datetime.datetime.now())
                #returns the json string
                return json_string

        """if the name is not there in the string, then we will store then we will store the name and other details in a dictionar.
        And at last, we will append this dictionary to a string"""
        #Storing the name in the dictionary
        dict1["name"] = c_name

        # Taking the share count and share price and stores it into the dictionary
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


        dict1["share_count"] = share
        dict1["share_price"] = price

        #Appends the dictionary to json string
        json_string.append(dict1)
        #returns the json string
        return json_string

    #Function to perform the sell operation
    def sell(self, json_string):
        #Takes the company name as the input
        c_name = ''
        while True:
            c_name = input("Enter the company name : ")
            if (c_name.isdigit()):
                print("Numbers are not allowed")
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

        #Finds the length of the json string
        len1 = len(json_string)
        #Loop iterates through all the elements of the json string
        for i in range(len1):
            #Checks whether the company name is same or not in each iteration
            if (c_name == json_string[i]["name"]):
                #takes the number of shares as input
                shares = 0
                while True:
                    try:
                        shares = int(input("Enter the number of shares : "))
                        if (shares < 1):
                            print("Share count should be a positive integer")
                            continue
                    except ValueError:
                        print("Share count should be a number")
                        continue
                    break
                #Checks whether the needed share is available or not
                if (shares > int(json_string[i]["share_count"])):
                    #If the shares are less, then print the message
                    print("Only ", json_string[i]["share_count"], " shares left, Please Re enter")
                    return json_string
                #If needed number of shares are available, then decrement the share count
                json_string[i]["share_count"] = int(json_string[i]["share_count"]) - shares
                return json_string
        print("The Given company is not available")