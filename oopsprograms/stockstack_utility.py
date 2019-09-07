class Stack:
    def __init__(self):
        #Initializes 'top' with '-1'
        self.top=-1
        #Initializes 'max' with '10'
        self.max=10
        #creates a list with 'max' number of elements with each element assignes as '0'
        self.list1=[0]*self.max

    #Function to push to the stack
    def push(self,json_string):
        #Checks whether the stack is full or not
        if(self.top == self.max):
            print("Stack is full")
            return
        #Incrementing 'top' by `1'
        self.top=self.top+1
        #Assigning json_string as the 'top' element
        self.list1[self.top]=json_string

    #Function to pop from the stack
    def pop(self):
        #Checks whether the stack is empty or not
        if(self.top == -1):
            print("Stack is empty")
            return
        #stores the 'top' element into a temp variable
        elem=self.list1[self.top]
        #Decrements 'top' by '1'
        self.top=self.top-1
        return elem

    #Function to check whether the stack is empty or not
    def isempty(self):
        #If 'top' value is '-1', then the stack is empty
        if(self.top == -1):
            return True