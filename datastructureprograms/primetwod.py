"""

    Name    : primetwod.py
    Date    : 31/08/2019
    Purpose : To find the Prime numbers in the range of 0 to 1000. Store the prime numbers in a 2D Array,

"""

from datastructureprograms import primetwod_utility

#getting the list of prime numbers by calling the makelist() method
list1=primetwod_utility.makelist()

#printing the prime numbers
for i in range(len(list1)):
    print(list1[i])
            
