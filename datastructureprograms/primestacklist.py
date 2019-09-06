"""

    Name    : primestacklist.py
    Date    : 31/08/2019
    Purpose : To Add the Prime Numbers that are Anagram in the Range of 0 - 1000 in a Stack using
              the Linked List and Print the Anagrams in the Reverse Order.

"""

from datastructureprograms import primestacklist_utility

#calls the function and gets the list of prime numbers in return
primelist = primestacklist_utility.makeprimelist()
print("PrimeList : ",primelist)

#creates list for anagrams
anagramlist=[]
#Ourter loop iterates through all the elements in the primelist
for i in primelist:
    #For every iteration of the outer loop, inner loop itertes through every element of the primelist
    for j in primelist:
        """passing two elements to the anagram() method to check whether those are anagram or not.
        If those are anagrams, control goes inside"""
        if(primestacklist_utility.anagram(i,j) == True):
            """Checks whether both the elements are same or not.
            If not same, then add those to the angramlist"""
            if i != j:
                anagramlist.append(i)
                anagramlist.append(j)

#Creates an object for the 'Stack' class
s1=primestacklist_utility.Stack()

#Iterates through the elements of angramlist.
for i in anagramlist:
    #Push each element in to the stack
    s1.push(i)
#Calling the display() method of stack
s1.display()

#Loop continues until the length of the anagramlist
for i in range(0,len(anagramlist)):
    #pop one element in each iteration
    a=s1.pop()
    #Print that element
    print(a)