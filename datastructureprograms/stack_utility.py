class Stack:

    def __init__(self):
        #Initializing 'top' with '-1' and 'max' with '10'
        self.top=-1
        self.max=10
        #creating a list with 'max' number of '0' elements
        self.stack_list = [0]*self.max

    def push(self,item):
        #if 'top' has reached 'max', then, stack is full,return
        if(self.top == self.max):
            print("Stack is full")
            return
        #increase the value of 'top' by '1'
        self.top=self.top+1
        #Assigning the 'item' to the 'top'
        self.stack_list[self.top]=item

    def pop(self):
        #pop the top most element by just decrementing the 'top' value by '1'
        self.top=self.top-1

    def peek(self):
        #if 'top' is '-1', then stack is empty,return
        if(self.top == -1):
            print("Stack is empty")
            return
        #return the topmost element of the stack
        return self.stack_list[self.top]

    def isempty(self):
        # if 'top' is '-1', then stack is empty,return
        if(self.top == -1):
            print("Stack is empty")
            return True
        # if 'top' is less than '-1', then ')' will be more than '('
        elif(self.top < -1):
            return False

    def size(self):
        # if 'top' is '-1', then stack is empty,return
        if(self.top == -1):
            print("Stack is empty")
            return
        #Initializing 'count' with '0'
        count=0
        #Iterates the loop till 'top' reaches '-1'
        while(self.top != -1):
            #Increasing the 'count' in each iteration
            count+=1
            #decreasing the value of 'top' by '1'
            self.top=self.top-1