class Node:
    def __init__(self,data):
        #Initializing the 'data' with the passed 'data' and 'next' with 'None'
        self.data=data
        self.next=None


class Stack:
    def __init__(self):
        #Initializing the 'head' with 'None'
        self.head=None

    #Function to check whether the stack is empty or not
    def isempty(self):
        #If the 'head' is 'None', stack is empty
        if self.head==None:
            return True
        else:
            return False

    #Function to push an element into the stack
    def push(self,data):
        if self.head==None:
            #If the head is none, create a node with the given data and make it as 'head'
            self.head=Node(data)
        else:
            new_node=Node(data)
            #If the 'head' is not 'None', make the 'new_node' as 'head' and place that node after the 'new_node'
            new_node.next=self.head
            self.head=new_node

    #Function to pop(remove) an element from the stack
    def pop(self):
        #checks whether the stack is empty or not by calling 'isempty()' method of stack
        if(self.isempty()):
            return None
        else:
            #storing the head node in a temperrary variabble
            popped_node=self.head
            #Assigning the next element as the head
            self.head=self.head.next
            #Removing the link from the deleting node to the next node
            popped_node.next=None
            #returning the popped node's data
            return popped_node.data

            #Function to get the data int he head node
    def peek(self):
        #Checking whether the stack is empty or not
        if(self.isempty()):
            return None
        else:
            #if it is not empty,return data in the head
            return self.head.data

    #Function for displaying the stack elements
    def display(self):
        # Checking whether the stack is empty or not
        if(self.isempty()):
            print("No elements in Stack")
        else:
            #starts from the head
            it=self.head
            #Loop continues until the last node
            while(it != None):
                print(it.data,' -> ', end=" ")
                it=it.next




def prime(i):
    for j in range(1,(i//2)+1):
        if i == 1:
            return False
        if(i%j != 0 or j==1):
            if(j== i//2):
                return True
        else:
            return False
def anagram(i,j):
    a=list(str(i))
    b=list(str(j))
    list.sort(a)
    list.sort(b)
    if a == b:
        return True
    else:
        return False
def makeprimelist():
    primelist = []
    for i in range(1,1000):
        if(prime(i) == True):
            primelist.append(i)
    return primelist