class Dequeue:

    def __init__(self,num):
        #Initializes the rear and front with '0'
        self.rear=0
        self.front=0
        #creates a list with the length as same as the length of the string, all the elements are made as '0'
        self.dequeuelist=[0]*(num+1)

    #Function to add the element at the rear
    def addRear(self,item):
        #adding the passed element to 'rear'
        self.dequeuelist[self.rear]=item
        #Increments the 'rear' by '1'
        self.rear=self.rear+1

    #Function to add the element at the front
    def addFront(self,item):
        # adding the passed element to 'front'
        self.dequeuelist[self.front]=item
        # Decrements the 'front' by '1'
        self.front=self.front-1

    #Function to remove the element from the 'front'
    def removeFront(self):
        #starting with front as '0'
        self.front=0
        #storing the 'front' element into a temp variable
        temp1=self.dequeuelist[self.front]
        #Incrementing 'temp'
        self.front=self.front+1
        #returning 'temp'
        return temp1

    #Function to remove the element fromm 'rear'
    def removeRear(self,count):
        #Decrementing 'rear' by '1'
        self.rear=self.rear-1
        #storing the element at the 'rear' to the 'temp' variable
        temp2=self.dequeuelist[self.rear]
        #Returning that element
        return temp2