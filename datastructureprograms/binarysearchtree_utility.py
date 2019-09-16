#Function to find the factorial of a number
def fact(num):
    #factorial of '2' is '1'
    if num < 2:
        return 1
    else:
        #Initializing 'f' and 'fact' with '1'
        f=1
        fact=1
        #Loop continues till 'f' reaches 'num'
        while(f != num+1):
            fact=fact*f
            #Increment the value of 'f' by '1' in every iteration
            f+=1
        #returns the final factorial value
        return fact

#Function to find the number of nodes
def find(n):
    if(str(n).isdigit()):
        #Applying the equation to find the number of nodes, fact() function is called here
        val=fact(2*n)//((fact(n+1)*fact(n)))%100000007
        print(val)
        return val
    else:
        return False