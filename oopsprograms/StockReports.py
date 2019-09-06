import json
import datetime
def displaystock(json_string):
    for i in range(len(json_string)):
        print("Name of the company : ",json_string[i]['name'])
        print("Share Count : ",json_string[i]['share_count'])
        print("Share Cost : ",json_string[i]['share_price'])
dict1={
    "name":None,
    "share_count":None,
    "share_price":None,
    "update_date":None
}

def buystock(json_string):
    c_name=input("Enter the company name : ")
    for i in range(len(json_string)):
        if(json_string[i]["name"] == c_name):
            json_string[i]['share_count']+=int(input("Enter the number of shares : "))
            json_string[i]['share_price']=int(input("Enter the share cost : "))
            json_string[i]['update_date']=str(datetime.datetime.now())
            return json_string
        
    dict1["name"]=c_name
    dict1["share_count"]=int(input("Enter the number of shares"))
    dict1["share_price"]=int(input("Enter the share price"))
    dict1["update_date"]=str(datetime.datetime.now())
    json_string.append(dict1)
    return json_string
def sellstock(json_string):

    c_name=input("Enter the company name : ")
    for i in range(len(json_string)):
        if(json_string[i]['name'] == c_name):
            s_count=int(input("Enter the number of shares"))
            if(json_string[i]['share_count'] < s_count):
                print("Insufficient shares")
                return
            else:
                json_string[i]['share_count']=json_string['share_count'] - s_count
                return json_string
    print("The given company is not available")

def file_open():
    try:
        with open("stock.json","r") as f:
            #json.dump(json_string,f)
            content=f.read()
 
        json_string=json.loads(content)
        return json_string
    except FileNotFoundError as e:
        print(e)


def file_update(json_string):
    try:
        with open("stock.json","w") as f:
            json.dump(json_string,f)
        return True
    except FileNotFoundError as e:
        print(e)    

if __name__ == "__main__":
    
    json_string =file_open()
    bool1="True"
    while(bool1 == "True"):
        displaystock(json_string)
        print("1.Display")
        print("2.Buy")
        print("3.Sell")
        n=int(input("Select an option : "))
        if(n == 1):
            displaystock(json_string)
        elif(n == 2):

            json_string=buystock(json_string)
            file_update(json_string)
            
        elif(n == 3):
            json_string=sellstock(json_string)
        bool1=input("Dou you want to continue : True or False")

        
    
