import json
import sys

class Exinvent:

    #Function to open the file
    def file_open(self):
        data=''
        try:
            #Opens the file with read permission
            with open("exinventory.json","r") as f:
                data=json.load(f)
        except FileNotFoundError as e:
            print(e)
            sys.exit()
        return data

    #Function to search
    def search(self,dict1,rtype,category):
        wt=0
        while True:
            try:
                wt=int(input("How much Kg you need ? :"))
                if(wt < 1):
                    print("Enter Positive integers only")
                break
            except ValueError:
                print("Enter weight in numbers only")
                continue

        #Checks whether the stock is available or not
        if(wt > dict1[category][rtype-1]["weight"]):
            #If not available, then prompt the user
            print("Only ",dict1[category][rtype-1]["weight"]," is left in stock. Please Re enter")
            return
        else:
            #If it is available, calculate the amount and display it
            print("Amount = ",wt*(dict1[category][rtype-1]["price"]))
            #Decrement the weight in stock
            dict1[category][rtype-1]["weight"]-=wt