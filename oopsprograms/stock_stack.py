import json
import datetime
class Stack:
    def __init__(self):
        self.top=-1
        self.max=10
        self.list1=[0]*self.max
    def push(self,json_string):
        if(self.top == self.max):
            print("Stack is full")
            return
        self.top=self.top+1
        self.list1[self.top]=json_string
    def pop(self):
        if(self.top == -1):
            print("Stack is empty")
            return
        elem=self.list1[self.top]
        self.top=self.top-1
        return elem
    def isempty(self):
        if(self.top == -1):
            return True



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
            s1.push(json_string[i])
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
            if(int(json_string[i]['share_count']) < s_count):
                print("Insufficient shares")
                return
            else:
                json_string[i]['share_count']=int(json_string[i]['share_count']) - s_count
                json_string[i]['update_date']=str(datetime.datetime.now())
                s1.push(json_string[i])
                return json_string
    print("The given company is not available")

def file_open():
    try:
        with open("stock.json","r",encoding='utf-8') as f:
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
    s1=Stack()
    bool1="True"
    while(bool1 == "True"):
        print("1.Display")
        print("2.Buy")
        print("3.Sell")
        print("4.Print the completed transactions")
        n=int(input("Select an option : "))
        if(n == 1):
            displaystock(json_string)
        elif(n == 2):
            json_string=buystock(json_string)
            file_update(json_string)
        elif(n == 3):
            json_string=sellstock(json_string)
            file_update(json_string)
        elif(n == 4):
            len1=len(json_string)
            print("Completed Transactions : ")
            print()
            for i in range(len1):
                if(s1.isempty() != True):
                    ele=s1.pop()
                    print(ele)
            

        
    
