class Queue:
    def __init__(self, num):
        #Initializes rear and front of the queue with '0'
        self.rear = 0
        self.front = 0
        self.num = num
        #Takes the total balance through input
        total=0
        while True:
            try:
                total = int(input("Enter the total balance left in bank : "))
                if(total < 1):
                    print("Amount should be a positive integer")
                    continue
                break
            except ValueError:
                print("Amount should be an integers")
                continue
        #Total amount is divided and assigned equally for each person
        perperson = int(total / num)
        """creates a list with the number of elements same as the number of people,
        and the equally divided value as the elements"""
        self.queuelist = [perperson] * (num)


    #Function for adding elements into the queue
    def enqueue(self, item):
        #Checks whether the queue is full or not
        if (self.rear == self.num):
            print(self.queuelist)
            print("No More People Allowed")
            return
        #adds the new element to the rear
        self.queuelist[self.rear] += item
        #Increments 'rear' by '1'
        self.rear = self.rear + 1


    #Function to remove the elements from the queue
    def dequeue(self, amount):
        print(self.front, amount)
        #Assigning element at the 'front' to 'x'
        x = self.queuelist[self.front]

        """Checks whether the given amount lesser than x or not.
        If it is lesser or equal, the 'amount' will be decremented from the element.
        or else, insufficient balance will be printed"""
        if (amount <= x):
            print('Transaction Successful')
            self.queuelist[self.front] = self.queuelist[self.front] - amount
        else:
            print("Insufficient balance in your account")
        print(self.queuelist)
        #Incrementing 'front'
        self.front = self.front + 1


    #function to check whether the queue is empty or not
    def isempty(self):
        if (self.rear == self.front):
            print("Queue is Empty")


    #Function to get the size of the queue
    def size(self):
        #starts with the front element
        cur = self.front
        count = 0
        #Loop continues until it reaches the 'rear'
        while (cur != self.rear):
            #Incrementing the 'count' value and decrementing the cur 'value'
            count += 1
            cur -= 1
        return count




