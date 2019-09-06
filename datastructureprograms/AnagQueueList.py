class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.front=self.rear=None
    def isEmpty(self):
        if(self.front == None):
            return True
    def enqueue(self,data):
        temp=Node(data)
        if(self.rear==None):
            self.rear=self.front=temp
        else:
            self.rear.next=temp
            self.rear=temp
    def dequeue(self):
        if(self.isEmpty()):
            return
        temp=self.front
        self.front=temp.next
        if(self.front == None): 
            self.rear = None
        return str(temp.data)
    def display(self):
        if self.front == None:
            return
        it=self.rear
        while(it != None):
            print(it," -> ",end=" ")
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
    for i in range(1,1000):
        if(prime(i) == True):
            primelist.append(i)

  

primelist=[]
makeprimelist()
print("PrimeList : ",primelist)
anagramlist=[]
for i in primelist:
    for j in primelist:
        if(anagram(i,j) == True):
            if i != j:
                anagramlist.append(i)
                anagramlist.append(j)
s1=Queue()
for i in anagramlist:
    s1.enqueue(i)
s1.display()
for i in range(0,len(anagramlist)):
    a=s1.dequeue()
    print(a)
