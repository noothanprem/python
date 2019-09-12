from oopsprograms.regularexpression_utility import Regex
import sys

#Creating the object of the Regex class
r1=Regex()
#Storing the string
str1="Hello <<name>>, We have your full name as <<full name>> in our system. your contact number is 91-xxxxxxxxxx. Please,let us know in case of any clarification Thank you BridgeLabz 01/01/2016."

while True:
    #Taking the name as the input from the user
    name=input("Enter your name : ")
    if(name.isdigit()):
        print("Numbers are not allowed")
        continue
    if(name.isspace()):
        print("White spaces are not alllowed")
        continue
    specialChars = ["$", "#", "@", "!", "*", "+", "-", ",", "%", "^", "(", ")", "[", "]", "{", "}", ":", ";",
                    "'", "<",
                    ">", "?", "~"]
    for i in name:
        for j in specialChars:
            if (i == j):
                print("No Special characters allowed.. Please try once more")
                sys.exit()
    break
#calling the function to replace the name
str2=r1.namereplace(str1,name)
print(str2)
#Taking the full name as the input from the user
while True:
    fname=input("Enter your full name : ")
    if(fname.isdigit()):
        print("Numbers are not allowed")
        continue
    if(fname.isspace()):
        print("White spaces are not alllowed")
        continue
    specialChars = ["$", "#", "@", "!", "*", "+", "-", ",", "%", "^", "(", ")", "[", "]", "{", "}", ":", ";",
                    "'", "<",
                    ">", "?", "~"]
    for i in fname:
        for j in specialChars:
            if (i == j):
                print("No Special characters allowed.. Please try once more")
                sys.exit()
    break
#calling the function to replace the full name
str3=r1.fullnamereplace(str2,fname)
print(str3)

while True:
    #Taking the mobile number as the input from the user
    num=input("Enter your mobile number ; ")
    if(num.isdigit() == False):
        print("Only numbers are allowed")
        continue
    if(num.isspace()):
        print("White spaces are not allowed")
        continue
    specialChars = ["$", "#", "@", "!", "*", "+", "-", ",", "%", "^", "(", ")", "[", "]", "{", "}", ":", ";",
                    "'", "<",
                    ">", "?", "~"]
    for i in num:
        for j in specialChars:
            if (i == j):
                print("No Special characters allowed.. Please try once more")
                sys.exit()
    break
#calling the function to replace the number
str4=r1.numberreplace(str3,num)
print(str4)

#calling the function to replace the date
str5=r1.datereplace(str4)
print(str5)