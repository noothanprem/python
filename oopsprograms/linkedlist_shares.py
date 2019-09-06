import json
import datetime
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def add(self,data):
        new_node=Node(data)
        if(self.head is None):
            self.head=new_node
            return
        cur_node=self.head
        while(cur_node.next != None):
            cur_node=cur_node.next
        cur_node.next=new_node
    def display(self):
        if(self.head is None):
            print("No element in the Linked List")
            return
        cur_node=self.head
        while(cur_node != None):
            print(cur_node.data)
            cur_node=cur_node.next
    def remove(self):
        elem=input("Enter the element which you want to remove : ")
        if(self.head is None):
            print("The list is empty")
            return
        elif(self.head.data["name"] == elem):
            cur_node=self.head
            self.head=cur_node.next
        else:   
            cur_node=self.head
            while(cur_node.next.data["name"] != elem):
                cur_node=cur_node.next
            temp=cur_node.next
            cur_node.next=temp.next
        list2=[]
        cur=self.head
        while(cur != None):
            list2.append(cur.data)
            cur=cur.next
        print(list2) 
        with open("stocks1.json","w") as f:
            json.dump(list2,f)  

        

        
        
class Jsoninteract:
    def file_open(self):
        with open("stocks1.json","r") as f:
            content=f.read()
            json_string=json.loads(content)
        return json_string
    def file_update(self,json_string):
        with open("stocks1.json","w") as f:
            json.dump(json_string,f)

    def add(self,json_string):
        dict1={
        "name":None,
        "share_count":None,
        "share_price":None,
        "update_date":None
        }
        dict1["name"]=input("Enter the company name : ")
        dict1["share_count"]=input("Enter the number of shares")
        dict1["share_price"]=input("Enter the share price : ")
        dict1["update_date"]=str(datetime.datetime.now())
        json_string.append(dict1)
        return json_string
        

if __name__ == "__main__":
    list1=LinkedList()
    j1=Jsoninteract()
    json_string=j1.file_open()
    for i in json_string:
        print(i)
        list1.add(i)
    c=1
    while(c == 1):
        print("1.Display")
        print("2.Add Share")
        print("3.Remove Share")
        op=int(input("Enter 1,2, or 3 : "))
        if(op == 1):
            list1.display()
        elif(op == 2):
            json_string=j1.add(json_string)
            list1.add(json_string)
            j1.file_update(json_string)
        elif(op == 3):
            list1.remove()
        c=int(input("Enter 1 to continue and 2 to exit : "))
        

