def prime(i):
    #Loop iterates from 1 to i/2
    for j in range(1,(i//2)+1):
        #1 is not a prime number
        if i == 1:
            return False
        """Checking whether i is divisible by the numbers in the range or j is 1 or not
        If it is true, it enters inside"""
        if(i%j != 0 or j==1):
            """checks whether we have checked with all the elements or not.
            If so, it is a prime number"""
            if(j== i//2):
                return True
        else:
            return False



def makelist():

    #creates a list
    list1=[]
    #creates a string
    str1=''
    s=0
    #It gives '0 to'
    str1=str(s)+' '+' to '
    #making 's' as '100'
    s=s+100
    #gives '0 to 100 '
    str2=str1+str(s)+'  '

    #creates new list
    list2=[]
    #Appending str2 to list2
    list2.append(str2)

    #Takes a rang of 1 to 1000 for finding the prime numbers
    for i in range(1,1000):
        #calls 'prime()' for checking whether it is prime or not
        if(prime(i) == True):
            #If it is prime, append it to list2
            list2.append(i)
        #checks whether it is a century(100,200,..etc) or not
        if i%100 == 0:
            str2=''
            #Used to display the range. It gets incremented in every iteration
            str2=str(s)+' to '
            s=s+100
            str2+=str(s)+' '

            #appends list2 to list1
            list1.append(list2)
            #makes the list to empty
            list2=[]
            #puts the range in list2
            list2.append(str2)
    #append list2 to list1
    list1.append(list2)
    #return list1
    return list1
