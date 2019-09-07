import json
import datetime

class Stockreports:

    def displaystock(json_string):
        #Number of iterations will be same as the length of the json_string
        for i in range(len(json_string)):
            #Accesses the fields of each and prints it
            print("Name of the company : ", json_string[i]['name'])
            print("Share Count : ", json_string[i]['share_count'])
            print("Share Cost : ", json_string[i]['share_price'])



    # Function to perform buy operation
    def buystock(json_string):
        # Takes the company name
        c_name = input("Enter the company name : ")
        # Loop iterates equal to the length of the string
        for i in range(len(json_string)):
            # Checks whether the name is same as the given name in each iteration
            if (json_string[i]["name"] == c_name):
                # If the name is found, then update the share_count and other details according to the user's input
                json_string[i]['share_count'] += int(input("Enter the number of shares : "))
                json_string[i]['share_price'] = int(input("Enter the share cost : "))
                json_string[i]['update_date'] = str(datetime.datetime.now())
                return json_string

            # creates a dictionary
            dict1 = {
                "name": None,
                "share_count": None,
                "share_price": None,
                "update_date": None
            }

        # If the given company is not available, then store all the information in a dictionary
        dict1["name"] = c_name
        dict1["share_count"] = int(input("Enter the number of shares"))
        dict1["share_price"] = int(input("Enter the share price"))
        dict1["update_date"] = str(datetime.datetime.now())
        # Append the dictionary to the json_string
        json_string.append(dict1)
        return json_string



    # Function to sell the stock
    def sellstock(json_string):
        # Takes the company name from the user
        c_name = input("Enter the company name : ")
        # Iterates through all the elements in the json string
        for i in range(len(json_string)):
            # Checks whether the given company is available or not
            if (json_string[i]['name'] == c_name):
                s_count = int(input("Enter the number of shares"))
                # If it is available, get the share_count they want to sell
                if (json_string[i]['share_count'] < s_count):
                    # If not available, prompt the user
                    print("Insufficient shares")
                    return
                else:
                    # If available, update the share_count and share_date
                    json_string[i]['share_count'] = int(json_string[i]['share_count']) - s_count
                    return json_string
        # If it comes out of the loop, that means, the company is not available
        print("The given company is not available")



    # Function to open the json file
    def file_open():
        try:
            # Opens the file with read permission
            with open("stock.json", "r") as f:
                # json.dump(json_string,f)
                content = f.read()

            json_string = json.loads(content)
            return json_string
        except FileNotFoundError as e:
            print(e)


    # Function to update the json file
    def file_update(json_string):
        try:
            with open("stock.json", "w") as f:
                json.dump(json_string, f)
            return True
        except FileNotFoundError as e:
            print(e)