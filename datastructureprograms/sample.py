#nums=[1,2,3,4,5,6,7,8,9,10]
#list1=[]
#for n in nums:
    #list1.append(n)
#print(list1)

##mylist = [n for n in nums]
##print(mylist)

#I want n*n for each n in nums
#list1=[]
#for n in nums:
    #list1.append(n*n)
#print(list1)

#mylist=[n*n for n in nums]
#print(mylist)

#I want n for each n in nums if n is even
#mylist=[]
#for n in nums:
    #if n%2 == 0:
        #mylist.append(n)
#print(mylist)

#mylist=[n for n in nums if n%2 == 0]
#print(mylist)

#I want a (letter,num) pair for each letter in 'abcd' and each number in '0123'
#mylist=[]
#for letter in 'abcd':
    #for n in range(4):
       # mylist.append((letter,n))
#print(mylist)

#mylist=[(letter,n) for letter in 'abcd' for n in range(4)]
#print(mylist)

#I want a dict{'name':'car'} for each name,car in zip(names,cars)
#names=['janis','thanzeeh','sreeraj','jettus','noothan']
#cars=['verna','alto','wagonr','duster','micra']
#mapped=zip(names,cars)
#mapped=set(mapped)
#print(mapped)
#my_dict={}
#for name,car in zip(names,cars):
    #my_dict[name]=car
#print(my_dict)

#my_dict={name:car for name,car in zip(names,cars) if name != 'thanzeeh'}
#print(my_dict)

nums=[1,2,1,4,6,8,3,4,8,3,2]
#my_set=set()
#for i in nums:
    #my_set.add(i)
#print(my_set)

my_set={n for n in nums}
print(my_set)
        


    
