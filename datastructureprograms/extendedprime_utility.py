#Function to check whether a number is prime or not
def prime(i):
    #check for the divisors till i/2
    for j in range(1,(i//2)+1):
        #1 is not a prime number
        if i == 1:
            return False
        """checks divisiblility by each number
        goes inside if it is not divisible,or else, it goes to the else block"""
        if(i%j != 0 or j==1):
            #If it is not divisible, check whether we have reached half of the number or npot
            if(j== i//2):
                #If we have reached, it is a prime number
                return True
        else:
            return False



def anagram(i,j):
    #making both i and j lists
    a=list(str(i))
    b=list(str(j))
    #sorting both the lists
    list.sort(a)
    list.sort(b)
    #checks whether both are same or not. If same, they are anangrams
    if a == b:
        return True
    else:
        return False




def makeprimelist():
    #crearting a list for prime numbers
    primelist=[]

    #Takes a range of 0 to 1000 for checking for the prime numbers
    for i in range(1,1000):
        """calling the 'prime() function to check whether the particular number is prime or not.
        If it is prime, then add it to the list"""
        if(prime(i) == True):
            primelist.append(i)

    #returns the list
    return primelist