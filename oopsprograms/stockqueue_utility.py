
class Node:

    def __init__(self,data):
        #Initializes the data with passed data
        self.data=data
        # Initializes the next with None
        self.next=None

class Queue:

    def __init__(self):
        #Initilizes rear and front with 'None'
        self.front=self.rear=None

    #Function to check whether the queue is empty or not
    def isEmpty(self):
        #Queue is empty if front is 'None'
        if(self.front == None):
            return True

    #Function to put the data into the queue
    def enqueue(self,data):
        #creating a new node with the given data
        temp=Node(data)
        #if the queue is empty, then assign the node as rear and front
        if(self.rear==None):
            self.rear=self.front=temp
        else:
            #Assigning new node as the next node of the current rear node
            self.rear.next=temp
            #making the new node as rear
            self.rear=temp

    #Function to remove an element from the queue
    def dequeue(self):
        #Checks whether the queue is empty or not
        if(self.isEmpty()):
            return
        #taking front node into a temp variable
        temp=self.front
        #Assigning the next node as the front node
        self.front=temp.next
        if(self.front == None):
            self.rear = None
        return str(temp.data)

    #Function to print all the elements in the Queue
    def display(self):
        #Checks whether the queue is empty or not
        if self.front == None:
            return
        #starts with rear element
        it=self.rear
        #Iterates until rear becomes 'None'
        while(it != None):
            print(it)