class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.head=None
    def enqueue(self,data):
        new_node=Node(data)
        if(self.head is None):
            self.head=new_node
        else:
            cur=self.head
            while(cur.next != None):
                cur=cur.next
            cur.next=new_node
    def dequeue(self):
        if(self.head is None):
            print("Queue is empty")
        else:
            cur=self.head
            self.head=cur.next
    def front(self):
        if(self.head is None):
            print("Queue is empty")
        else:
            temp=self.head.data
            cur=self.head
            self.head=cur.next
        return temp
    def display(self):
        if(self.head is None):
            print("Queue is empty")
        else:
            cur=self.head
            while(cur != None):
                print(cur.data)
                cur=cur.next

def prime():
    for i in range(1,1000):    
        for j in range(1,(i//2)+1):
            if(i % j != 0 or j == 1):
                if(j == i//2):
                    primelist.append(i)    
            else:
                break
def anagram(i,j):
    a=list(str(i))
    b=list(str(j))
    a.sort()
    b.sort()
    if(a == b):
        return True
    else:
        return False


q1=Queue()
primelist=[]
prime()
print(primelist)
anagramlist=[]
for i in primelist:
    for j in primelist:
        if(anagram(i,j)):
            if(i != j):
                anagramlist.append(i)
print(anagramlist)
len1=len(anagramlist)

size=0
for i in anagramlist:
    q1.enqueue(i)
    size+=1

for i in range(size):
    elem=q1.front()
    print(elem)