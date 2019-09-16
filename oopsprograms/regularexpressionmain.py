import re
from datetime import date

class Regex:


    def namereplace(self,s1, s2):
        #Assigning passed s1 and s2 to str1 and name
        str1 = s1
        name = s2
        #regular expression to search for the 'name'
        p1 = '<<[a-z]{4}>>'
        # replaces the name with the given name
        str2 = re.sub(p1, name, str1)
        return str2

    def fullnamereplace(self,s1, s2):
        str1 = s1
        name = s2
        # regular expression to search for the 'full name'
        p1 = "<<[a-z]{4}\s[a-z]{4}>>"
        #replaces the full name with the given full name
        str2 = re.sub(p1,name, str1)
        return str2

    def numberreplace(self,s1, n):
        str1 = s1
        num = n
        # regular expression to search for the 'mobile number'
        p1 = "x{10}"
        # replaces the number with the given number
        str3 = re.sub(p1, str(num), str1)
        return str3

    def datereplace(self,s1):
        str2 = s1
        today = str(date.today())
        #replaces the date with the current date
        str3 = re.sub('\d{2}\/\d{2}\/\d{4}', today, str2)
        return str3