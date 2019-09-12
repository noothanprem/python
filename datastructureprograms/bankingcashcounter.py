"""

    Name : bankingcashcounter.py
    Date : 31/08/2019
    Purpose : To create Banking Cash Counter where people come in to deposit Cash and withdraw Cash

"""

from datastructureprograms.queue_utility import Queue

while True:
    try:
        #Getting the number of people
        n = int(input("Enter the number of people : "))
        if(n < 1):
            print("Number of people cannot be negative integers")
            continue
        break
    except ValueError:
        print("Enter the integers only")
        continue

#Creating th Queue class object
queue1 = Queue(n)
people=0
#Exectes till every user completes one deposit and one withdraw transactions
while(people <= n*2):
    mode=0
    while True:
        try:
            mode=int(input("Do you want to deposit(1) or withdraw(2) : "))
            if((mode != 1) and mode != 2):
                print("Enter either 1 or 2")
                continue
            break
        except ValueError:
            print("Enter either  1 or 2 ")
            continue
    if(mode == 1):
        #If the user wants to deposit, ask for the amount
        while True:
            try:
                amount = int(input("How much you want to deposit ?"))
                if(amount < 1):
                    print("Amount should be a positive integer")
                    continue
                break
            except ValueError:
                print("Amount should be a positive integer")
                continue
        #add the amount to the queue
        queue1.enqueue(amount)
    else:
        # If the user wants to withdraw, ask for the amount
        while True:
            try:
                amount = int(input("How much you want to withdraw ?"))
                if (amount < 1):
                    print("Amount should be a positive integer")
                    continue
                break
            except ValueError:
                print("Amount should be a positive integer")
                continue
        #Removes the amount from the queue
        queue1.dequeue(amount)
    people += 1
    

        
        


