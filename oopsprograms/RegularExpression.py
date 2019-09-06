import re
from datetime import date
def namereplace(s1,s2):
    str1=s1
    name=s2
    p1="<<name>>"
    str2=re.sub(p1,name,str1)
    return str2
def fullnamereplace(s1,s2):
    str1=s1
    name=s2
    p1="<<full name>>"
    str2=re.sub(p1,name,str1)
    print(str2)
def numberreplace(s1,n):
    str1=s1
    num=n
    p1="x{10}"
    str2=re.sub(p1,num,str1)
    print(str2)
def datereplace(s1):
    str2=s1
    today=str(date.today())
    print(type(today))
    st3=re.sub('\d{4}\/\d{2}\/\d{4}',today,str2)

str1="Hello <<name>>, We have your full name as <<full name>> in our system. your contact number is 91-xxxxxxxxxx. Please,let us know in case of any clarification Thank you BridgeLabz 01/01/2016."
name=input("Enter your name : ")
str2=namereplace(str1,name)
fullname=input("Enter the full name")
str3=fullnamereplace(str2,fullname)
num=input("Enter your mobile number")
#str4=numberreplace(str2,num)
str5=datereplace(str3)
