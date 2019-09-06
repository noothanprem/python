
import json

class Exinvent:
    def file_open(self):
        with open("exinventory.json","r") as f:
            data=json.load(f)
        return data
    def search(self,dict1,rtype,category):
        wt=int(input("How much Kg you need ? :"))
        if(wt > dict1[category][rtype-1]["weight"]):
            print("Only ",dict1[category][rtype-1]["weight"]," is left in stock. Please Re enter")
            return
        else:
            print("Amount = ",wt*(dict1[category][rtype-1]["price"]))
            dict1[category][rtype-1]["weight"]-=wt




if __name__ == "__main__":
    ex=Exinvent()
    dict1=ex.file_open()
    print(dict1)
    bool1=1
    while(bool1 == 1):
        print("1.rice")
        print("2.pulses")
        print("3.wheats")
        category=input("Enter what you want : ")
        print("Select from the following types : ")
        for i in range(3):
            print(i+1,". ",dict1[category][i]["name"])
        rtype=int(input("Enter the option : "))
        ex.search(dict1,rtype,category)
        bool1=int(input("Enter 1 to continue or 2 to exit : "))

    

    
