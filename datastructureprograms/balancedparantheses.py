"""

    Name : balancedparantheses.py
    Date : 31/08/2019
    Purpose : To Ensure parentheses in an arithematic expression must appear in a balanced fashion.

"""

from datastructureprograms.stack_utility import Stack

stack1 = Stack()
expr = input("Enter the arithmetic expression :")
for i in expr:
    if(i == '('):
        stack1.push(i)
    elif(i == ')'):
        stack1.pop()
if(stack1.isempty()):
    print("Parantheses are Balanced")
else:
    print("Parantheses are not balanced")


