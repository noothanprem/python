"""

    Name : extendedprime.py
    Date : 31/08/2019
    Purpose : To create Banking Cash Counter where people come in to deposit Cash and withdraw Cash

"""

from datastructureprograms import extendedprime_utility
  
#calling the makeprimelist() method in extendedprime_utility
primelist=extendedprime_utility.makeprimelist()
print("PrimeList : ",primelist)

#creating a list named anagramlist
anagramlist=[]

#outer loop iterates over all the elements in the list
for i in primelist:
    #for each iteration of the outer loop, inner loop iterates over all the list elements
    for j in primelist:
        #checking whether the two are anagrams or not
        if(extendedprime_utility.anagram(i,j) == True):
            """Checking whether those two are same or not.
            If not same, add those two to the anagramlist"""
            if i != j:
                anagramlist.append(i)
                anagramlist.append(j)
print("Anagram List : ",anagramlist)

#creating a new list for storing non-anagram numbers
notanaglist=[]

for i in range(len(primelist)):
    """checking whether the particular element in the primelist is there in the anagramlist or not.
    If it is not there, add it to the notanaglist"""
    if primelist[i] not in anagramlist:
        notanaglist.append(primelist[i]) 
print("Not Anagram List : ",notanaglist)
            
