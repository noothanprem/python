import json

class Inventory:

    def find():
        #Opens the json file for reading the data
        with open("inventory.json","r") as f:
            data=json.load(f)
        #Iterates through all the data
        for i in data:
            print(i)
            #Displays the name of each item and price
            print(i, data[i]["name"], data[i]["weight"]* data[i]["price"])
