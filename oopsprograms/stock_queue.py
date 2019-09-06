import json
import datetime
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.front=self.rear=None
    def isEmpty(self):
        if(self.front == None):
            return True
    def enqueue(self,data):
        temp=Node(data)
        if(self.rear==None):
            self.rear=self.front=temp
        else:
            self.rear.next=temp
            self.rear=temp
    def dequeue(self):
        if(self.isEmpty()):
            return
        temp=self.front
        self.front=temp.next
        if(self.front == None): 
            self.rear = None
        return str(temp.data)
    def display(self):
        if self.front == None:
            return
        it=self.rear
        while(it != None):
            print(it)



def displaystock(json_string):
    print(json_string)
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
            json_string[i]['share_count']=int(json_string[i]['share_count'])+int(input("Enter the number of shares : "))
            json_string[i]['share_price']=int(input("Enter the share cost : "))
            json_string[i]['update_date']=str(datetime.datetime.now())
            q1.enqueue(json_string[i])
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
                q1.enqueue(json_string[i])
                return json_string
    print("The given company is not available")

def file_open():
    try:
        with open("stock.json","r",encoding='utf-8') as f:
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
    q1=Queue()
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
            while(q1.isEmpty() != True):
                ele=q1.dequeue()
                print(ele)