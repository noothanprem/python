class node:
    def __init__(self, data):
        #Initializes 'data' with the passed 'data' and 'next' with 'None'
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        #Initializes 'head' with 'None'
        self.head = None

    #Function to add the data to the Linked List
    def add(self, data):
        #creates a new node with the passed 'data'
        new_node = node(data)
        #considering 'cur' as 'head'
        cur = self.head

        #if cur(or head) is 'None', then make new node as 'head
        if cur is None:
            self.head = new_node
            return

        #Loop continues until next node of the current node becomes null
        while cur.next is not None:
            cur = cur.next
        #places the new node as the last node
        cur.next = new_node


    #Function to find the size of the Linked List
    def size(self):
        #considering 'cur' as 'head'
        cur = self.head
        #Initializing the count variable 'total' with '0'
        total = 0

        #Loop continues until next node of the current node becomes null
        while cur.next is not None:
            #increments 'total' by 1 in every iteration
            total += 1
            cur = cur.next
        #returns the 'total'
        return total

    #Function to display the elements in the Linked List
    def display(self):
        #creates a list
        elems = []
        #checks whether the list is empty or not
        if self.head is None:
            return elems
        #makes the 'cur_node' the 'head'
        cur_node = self.head

        #Loop iterates until cur_node becomes null
        while cur_node is not None:
            #appends each node's data to the list in each iteration
            elems.append(cur_node.data)
            cur_node = cur_node.next
        #printing the list
        print(elems)

    #Function to get the specified element
    def get(self, index):
        #checks whether the index is valid
        if index > self.size():
            print("Enter a Valid index")
            return
        #takes the cur_index as '0'
        cur_index = 0
        #takes cur_node as 'head'
        cur_node = self.head
        while True:
            """checks whether the 'cur_index' is same as passed 'index' or not.
            If so, then return the data in that node"""
            if(cur_index == index):
                return cur_node.data
            #Move to the next node and also increment the index count
            cur_node = cur_node.next
            cur_index += 1


    #Function to remove an element from the linked list
    def remove(self, index):
        #checks whether the index is valid or not
        if index > self.size():
            print("Enter a valid index")
            return
        #Checks whether the linked list is empty or not
        if self.head is None:
            return
        #Setting the cur_index as '0'
        cur_index = 0
        #taking cur_node as self.head
        cur_node = self.head
        #If the index is '0', assign the next element of the 'head' as the 'head'
        if index == 0:
            self.head = self.head.next
        #Iterates until index becomes 1 and next node becomes 'None'
        while index > 1 and cur_node.next != None:
            index -= 1
            cur_node = cur_node.next
        if cur_node == None and cur_node.next == None:
            return
        tem = cur_node.next.next
        cur_node.next = tem


    def delete(self, item, index):
        if (index == 0):
            self.head = self.head.next
            self.display()
            return
        cur_index = 0
        cur_node = self.head
        while cur_index < index:
            last_node = cur_node
            cur_node = cur_node.next
            if (cur_index == (index - 1)):
                last_node.next = cur_node.next
            cur_index += 1
        self.display()


    #Function to search for an item in the list
    def search(self, item):
        #checks whether the linked list is empty or not
        if self.head is None:
            return
        #Setting the cur_node as 'head' node
        cur_node = self.head
        #starts with index as '0'
        index = 0
        #Loop iterates until the cur_node becomes 'None'
        while cur_node != None:
            """Compares the data with each node's data,whether they are equal or not
            if they are equal, call the delete() method"""
            if item == cur_node.data:
                self.delete(item, index)
                return
            #Increment the index and move to the next node
            index += 1
            cur_node = cur_node.next
        #If it comes out of the loop after all iterations, that means item is not there in that list
        print("Item not Found")
        #Add that item if the item is not found
        self.add(item)
        self.display()

    #Function to return the data in the 'head' node
    def da(self):
        return self.head.data