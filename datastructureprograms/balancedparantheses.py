"""

    Name : balancedparantheses.py
    Date : 31/08/2019
    Purpose : To Ensure parentheses in an arithematic expression must appear in a balanced fashion.

"""

from datastructureprograms.stack_utility import Stack
stack1=Stack()
class Balanced:

    def check(expr):
        if(expr == " "):
            return False
        specialChars = ["$", "#", "@", "!", "*", "+", "-", ",", "%", "^","[", "]", "{", "}", ":", ";",
                        "'", "<",
                        ">", "?", "~"]
        for j in specialChars:
            if (j == expr):
                print("No Special characters allowed.. Please try once more")
                return False



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
            return True
        else:
            print("Parantheses are not balanced")
            return False

    def input1():
        #Getting the arithematic expression from the user
        expr = input("Enter the arithmetic expression :")
        return expr








