import re
from datetime import date

class Regex:

    def namereplace(s1, s2):
        str1 = s1
        name = s2
        p1 = "<<name>>"
        str2 = re.sub(p1, name, str1)
        return str2

    def fullnamereplace(s1, s2):
        str1 = s1
        name = s2
        p1 = "<<full name>>"
        str2 = re.sub(p1, name, str1)
        print(str2)

    def numberreplace(s1, n):
        str1 = s1
        num = n
        p1 = "x{10}"
        str2 = re.sub(p1, num, str1)
        print(str2)

    def datereplace(s1):
        str2 = s1
        today = str(date.today())
        print(type(today))
        st3 = re.sub('\d{4}\/\d{2}\/\d{4}', today, str2)