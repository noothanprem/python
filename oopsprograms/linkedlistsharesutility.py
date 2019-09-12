import json
import datetime
import sys

class Node:

    def __init__(self, data):
        #Initializes the 'data' with the passed 'data'
        self.data = data
        #Initializes 'next' with 'None'
        self.next = None


class LinkedList:
    def __init__(self):
        #Initializes 'head' of the Linked List with 'None'
        self.head = None

    #Function to add a node to the LinkedList
    def add(self, data):
        #creates a new node with the given data
        new_node = Node(data)
        #If Linked List does not contain anything, then make the new_node as the head
        if (self.head is None):
            self.head = new_node
            return
        #Start with the head node
        cur_node = self.head
        #Moves from head node and stops when the next node is 'None'
        while (cur_node.next != None):
            cur_node = cur_node.next
        #put the new node as the last node
        cur_node.next = new_node


    #Function to display the List contents
    def display(self):
        #If the head is 'None', then the Linked List will be empty
        if (self.head is None):
            print("No element in the Linked List")
            return
        #Starts with the head node
        cur_node = self.head
        #Moves from head node and stops when the current node is 'None'
        while (cur_node != None):
            #prints the data in each node
            print(cur_node.data)
            cur_node = cur_node.next


    #Function to remove a node
    def remove(self):
        while True:
            #gets the name of the element which the user wants to remove
            elem = input("Enter the element which you want to remove : ")
            if(elem.isdigit()):
                print("Numbers are not allowed")
                continue
            if(elem.isspace()):
                print("Whitespaces are not allowed")
                continue
            specialChars = ["$", "#", "@", "!", "*", "+", "-", ",", "%", "^", "(", ")", "[", "]", "{", "}", ":", ";",
                            "'", "<",
                            ">", "?", "~"]
            for i in elem:
                for j in specialChars:
                    if (i == j):
                        print("No Special characters allowed.. Please try once more")
                        sys.exit()

            break


        #If the head node is 'None', then the Linked List will be empty
        if (self.head is None):
            print("The list is empty")
            return
        elif (self.head.data["name"] == elem):
            """Checks whether the name given is same as the name in the head node.
            If same, then make the next node as the head node"""
            cur_node = self.head
            self.head = cur_node.next
        #
        else:
            #Starts from the head and iterates throug all the nodes in the linked list till it finds the same name
            cur_node = self.head
            while (cur_node.next.data["name"] != elem):
                cur_node = cur_node.next
            #Assigning next node to a temp variable
            temp = cur_node.next
            #making the 'next'' link to point to the node after that node
            cur_node.next = temp.next
        list2 = []
        #starts from the head node and iterates till it finds an empty node
        cur = self.head
        while (cur != None):
            #Append each node's data to a list
            list2.append(cur.data)
            cur = cur.next
        print(list2)
        try:
            #dumps the data in the list to the json file
            with open("stocks1.json", "w") as f:
                json.dump(list2, f)
        except FileNotFoundError as e:
            print(e)
            sys.exit()



class Jsoninteract:

    #Function to open the json file
    def file_open(self):
        try:
            #Opens the file with 'read' permission
            with open("stocks1.json", "r") as f:
                content = f.read()
                json_string = json.loads(content)
        except FileNotFoundError as e:
            print(e)
            sys.exit()

        return json_string

    #Function to update the json file
    def file_update(self, json_string):
        try:
            # Opens the file with 'write' permission
            with open("stocks1.json", "w") as f:
                json.dump(json_string, f)
        except FileNotFoundError as e:
            print(e)
            sys.exit()

    #Function To add a new company
    def add(self, json_string):
        #creates a dictionary to add the company
        dict1 = {
            "name": None,
            "share_count": None,
            "share_price": None,
            "update_date": None
        }
        #Taking the inputs from the user and adding to the dictionary
        dict1["name"] = input("Enter the company name : ")
        dict1["share_count"] = input("Enter the number of shares")
        dict1["share_price"] = input("Enter the share price : ")
        dict1["update_date"] = str(datetime.datetime.now())
        #Appending the dictionary to the json string
        json_string.append(dict1)
        return json_string