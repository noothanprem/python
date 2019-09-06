"""

    Name : bankingcashcounter.py
    Date : 31/08/2019
    Purpose : To create Banking Cash Counter where people come in to deposit Cash and withdraw Cash

"""

from datastructureprograms.queue_utility import Queue

n = int(input("Enter the number of people : "))
queue1 = Queue(n)
people=0
while(people <= n*2):
    mode=int(input("Do you want to deposit(1) or withdraw(2) : "))
    if(mode == 1):
        amount = int(input("How much you want to deposit ?"))
        queue1.enqueue(amount)
    else:
        amount=int(input("Enter How much You Want to Withdraw : "))
        queue1.dequeue(amount)
    people += 1
    

        
        


