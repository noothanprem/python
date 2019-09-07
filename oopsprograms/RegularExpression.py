from oopsprograms.regularexpression_utility import Regex

r1=Regex()
str1="Hello <<name>>, We have your full name as <<full name>> in our system. your contact number is 91-xxxxxxxxxx. Please,let us know in case of any clarification Thank you BridgeLabz 01/01/2016."
name=input("Enter your name : ")
str2=r1.namereplace(str1,name)
fullname=input("Enter the full name")
str3=r1.fullnamereplace(str2,fullname)
num=input("Enter your mobile number")
#str4=numberreplace(str2,num)
str5=r1.datereplace(str3)
