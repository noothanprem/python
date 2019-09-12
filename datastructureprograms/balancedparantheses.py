"""

    Name : balancedparantheses.py
    Date : 31/08/2019
    Purpose : To Ensure parentheses in an arithematic expression must appear in a balanced fashion.

"""

from datastructureprograms.stack_utility import Stack

#Creating the object for Stack class
stack1 = Stack()

#Getting the arithematic expression from the user
expr = input("Enter the arithmetic expression :")

for i in expr:
    #Pusing in to the stack if '(' is found
    if(i == '('):
        stack1.push(i)
    # Poping last '(' from the stack if ')' is found
    elif(i == ')'):
        stack1.pop()

#If stack is empty, parentheses are balanced, otherwise, not
if(stack1.isempty()):
    print("Parantheses are Balanced")
else:
    print("Parantheses are not balanced")


