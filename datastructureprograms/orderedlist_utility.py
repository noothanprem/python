
class node:
    def __init__(self, data):
        #Initializes the 'data' with the data passed and 'next' with 'None'
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        #Initializing 'head' as 'None'
        self.head = None

    #Function for adding new node to the linked list
    def add(self, data):
        #creating a new node with passed data
        new_node = node(data)
        #initializing 'cur' with 'head'
        cur = self.head

        """checking whether 'head' is 'None' or not.
        If it is 'None', new node will be the head """
        if cur is None:
            self.head = new_node
            return
        """Checking if the data in the 'head' is greater than the given data.
        If it is greater, set new node as the head """
        if cur.data > data:
            new_node.next = self.head
            self.head = new_node
            return
        #loop iterates till cur.next becomes null
        while cur.next is not None:
            """Checking if the data in any node's next node is greater than the given data.
            If it is greater, place the new node before that node"""
            if (data < cur.next.data):
                new_node.next = cur.next
                cur.next = new_node
                return
            cur = cur.next
        #If all the elements are lesser, then place it at last
        cur.next = new_node


    #Function for getting the size of the Linked List
    def size(self):
        #starts with the 'head' element
        cur = self.head
        #Initializing the counter 'total' with '0'
        total = 0

        #Loop gets iterated till next node is 'None'
        while cur.next is not None:
            total += 1
            cur = cur.next

        #returns the count
        return total



    #Function to display the elements of LinkedList
    def display(self):
        #creating a list for storing the elements in the linked list
        elems = []
        #if the head node is 'None', then the Linked list is empty
        if self.head is None:
            return elems
        #Starts with the head node and iterates through all the nodes in the list
        cur_node = self.head
        while cur_node is not None:
            #Appending each node's elements to the list
            elems.append(cur_node.data)
            cur_node = cur_node.next
        print(elems)

    #Function to get an element at a specified index
    def get(self, index):
        #Checks whether the index is valid or not
        if index > self.size():
            print("Enter a Valid index")
            return
        #Starts with an index value of '0' and 'head' as 'node'
        cur_index = 0
        cur_node = self.head

        while True:
            """Checks for the index.
            If it is the same, returns the data at that node"""
            if (cur_index == index):
                return cur_node.data
            cur_node = cur_node.next
            cur_index += 1

    #Method for removing a particular element
    def remove(self, index):
        # Checks whether the index is valid or not
        if index > self.size():
            print("Enter a valid index")
            return
        #Checks whether the Linked List is empty or not
        if self.head is None:
            return
        #Starts with '0' as the 'index' and 'cur_node' as 'head'
        cur_index = 0
        cur_node = self.head
        #Returns the 'head' element if the 'index' is '0'
        if index == 0:
            self.head = self.head.next
        #Loop continues till index becomes 1 and next node becomes 'None'
        while index > 1 and cur_node.next != None:
            #Decrementing the index
            index -= 1
            #Moving to the next node
            cur_node = cur_node.next

        #return if both the cur_node and the next node are 'None'
        if cur_node == None and cur_node.next == None:
            return
        tem = cur_node.next.next
        cur_node.next = tem


    #Function for deleting a node
    def delete(self, item, index):
        #If index is '0', then removes the 'head' node and sets the next node as 'head'
        if (index == 0):
            self.head = self.head.next
            self.display()
            return

        #starts with '0' as the 'index' and 'head' as the 'cur_node'
        cur_index = 0
        cur_node = self.head
        #Loop continues until 'index' reaches the needed 'index'
        while cur_index < index:
            #Removes the node
            last_node = cur_node
            cur_node = cur_node.next
            if (cur_index == (index - 1)):
                last_node.next = cur_node.next
            cur_index += 1
        self.display()


    #Function to search nfor an element in the Linked List
    def search(self, item):
        #If the 'head' is "None', then return
        if self.head is None:
            return
        #starts with head and '0' as 'index'
        cur_node = self.head
        index = 0
        #Loop continues until current node is 'None'
        while cur_node != None:
            """Checks whether the data in the cur_node is same as the passed value or not.
            If it's the same, delete that node by calling delete() method"""
            if item == cur_node.data:
                self.delete(item, index)
                return
            index += 1
            cur_node = cur_node.next
        "If it reaches the end, the element is not there in the Linked List"
        print("Item not Found")
        self.add(item)

    #Function for returning the data in the 'head' node
    def da(self):
        return self.head.data

