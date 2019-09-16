import json

class Inventory:

    def file_open(self):
        try:
            #Opens the json file for reading the data
            with open("inventory.json","r") as f:
                data=json.load(f)
        except FileNotFoundError as e:
            print(e)
        return data

    def find(self,data):
        #Iterates through all the data
        for i in data:
            #Displays the name of each item and price
            print(i, data[i]["name"], data[i]["weight"]* data[i]["price"])

