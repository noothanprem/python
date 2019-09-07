import json

class Exinvent:

    #Function to open the file
    def file_open(self):
        #Opens the file with read permission
        with open("exinventory.json","r") as f:
            data=json.load(f)
        return data

    #Function to search
    def search(self,dict1,rtype,category):
        wt=int(input("How much Kg you need ? :"))
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