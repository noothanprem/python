"""

    Name : binarysearchtree.py
    Date : 31/08/2019
    Purpose : To find the number of different binary search trees that can be created using the given number of nodes

"""


from datastructureprograms import binarysearchtree_utility

#getting the number of nodes from the user
n=int(input("Enter the number of nodes : "))

#Calling the function in the BL file
binarysearchtree_utility.find(n)