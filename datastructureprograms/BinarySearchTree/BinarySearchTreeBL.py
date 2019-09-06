def fact(num):
    if num < 2:
        return 1
    else:
        f=1
        fact=1
        while(f != num+1):
            fact=fact*f
            f+=1
        return fact

def find(n):
    val=fact(2*n)//((fact(n+1)*fact(n)))%100000007
    print(val)