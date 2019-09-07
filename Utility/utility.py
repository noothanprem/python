import math
import random
import time

def dis(x,y):
    #Applying the equation
    distance = math.sqrt(pow(x,2)+pow(y,2))

    #returning the result
    return distance



def gambler(stake, goal):
    ##Initializing the variables with 0
    count = 0
    win = 0
    lose = 0
    stake1 = stake
    goal1 = goal

    # continues till stake reaches the goal amount
    while (stake1 < goal1):

        # generating a random number between 0 and 1 and checking whether it is less than or greater than 0.5
        # if it is less than 0.5, we consider it as a win, else we consider it as lose
        if (random.random() < 0.5):
            win += 1
            stake1 += 1
            print("You won. Your new Stake is : ", stake1)
            count += 1
            continue
        else:
            lose += 1
            stake1 -= 1
            count += 1
            print("You lose, your new stake is : ", stake1)

            # come out if the stake becomes 0
            if (stake1 < 1):
                print("You have no stake left, your game is over")
                break
    # printing the number of wins & loses
    print("Total Number of wins : ", win)
    print("Total Number of Lose : ", lose)

    # Calculating the percentages
    winper = (win / count) * 100
    loseper = (lose / count) * 100

    # Printing the Percentages
    print("Win Percentage : ", winper)
    print("Lose Percentage : ", loseper)




def harmonic(n):

    # initializing harm variable to 0.0 and i to 1
    harm = 0.0
    i = 1

    # perform the opertation if the input is not 0
    if (n != 0):
        while (i <= n):
            harm = harm + (1 / i)
            i += 1
        # returning the harmonic value
        return round(harm, 2)
    else:
        print("Enter a Valid Number")




def headstails(n):
    num=n
    heads=0
    tails=0
    for i in range(num):
        toss=random.random()
        if toss < 0.5:
            print("heads")
            heads+=1
        else:
            print("tails")
            tails+=1
    headsper=(heads/num)*100
    tailsper=(tails/num)*100
    print("Heads Percentage : ",round(headsper,2))
    print("Tails Percentage : ",round(tailsper,2))



def leap(y):
    year=y
    #initializing the 'count' variable with 0
    count=0

    # checking whether it is a leap year
    if(year % 4 == 0 and year % 100 != 0 and year % 400 != 0):
        print(year," is a Leap Year")
    else:
        print(year, " is not a Leap Year")



def pow1(n):
    #Initializing the 'num' variable with the value of 'n' passed to the function
    num=n

    print("Powers of 2 : ")
    #Initializing the 'power' and 'i' valriables with 0
    power1=0
    i=0
    while(power1 < 2**num):
        #Performng the operation and printing the results till i reaches 'num'
        power1=2**i
        print("2**",i," = ",power1)
        i+=1



def stop():
    try:
        a=input("Do you want to start ? ... give true or false")
        if(a == True):
            start=time.time()
            print(start)
            b=input("Do you want to stop?... give True or False")
            if(b == True):
                end=time.time()
                print(end)
            print("The difference : ",end-start)
    except ValueError:
        print("Enter a boolean value")



def strreplace(s1,s2):

    str1=s1
    str2=s2

    #using 'replace' function of string
    string3 = str1.replace("user",str2)

    return string3





def sum(n,list1):
    #assigning the passed list 'list1' to 'list2' and n to num
    list2=list1
    num=n

    #initializing the 'count' with 0
    count=0

    print("Distinct triplets with sum as zero are :")
    #from 0th elment to n-3 th element
    for i in range(0,num-2):
        #from 1st element to n-2 th element
        for j in range(1,num-1):
            #from 2nd element to n-1 th element
            for k in range(2,num):
                #checking whether the sum of 3 digits is zero or not
                if(list1[i]+list1[j]+list1[k] == 0):
                    #if the sum is '0', pprinting thode 3 digits
                    print(list1[i]," , ",list1[j],",",list1[k])
                    #Incrementing the count variable
                    count+=1

    #Printing the count
    print("Total number of triplets : ",count)




def checkanagram(str1,str2):
    #Assgning the passed strings 'str1' and 'str2' to s1 and s2
    s1=str1
    s2=str2

    #finding the length of both s1 and s2
    len1=len(s1)
    len2=len(s2)

    #i from index 0 to len1-1
    for i in range(0,len1):
        #j from index 0 to len2-1
        for j in range(0,len2):
            #checking whether each character of s1 is present in s2 or not
            if(s1[i] == s2[j]):
                #checking whether we have reached the last character of s1 or not
                if(i == (len1-1)):
                    print("These are Anagrams")
                    return
                else:
                    #if it's not the last charcter, break the inner loop to continue with the next element of s1
                    break
            else:
                if(j == (len2-1)):
                    #checking whether we have reached the last character of s2 or not
                    #If we have reached, that means that character is not present in s2
                    #So, print the message saying that these are not Anagrams and return
                    print("These are not anagrams")
                    return
    print("These are not Anagrams")






def date(mn,dt,yr):
    #assigning the passed mn,dt,yr to month,date and year
    month=mn
    date=dt
    year=yr

    #Calculating the date using the formula
    y=year-(14-month)//12
    x=y + y//4 - y//100 + y//400
    m=month + 12*((14-month)//12)-2
    d=(date+x+31*m//12) % 7
    return d




def binary(list1, s):
    # Assigning the passed list1 and s to content and s1
    content = list1
    s1 = s

    # Initializing first and last
    first = 0
    last = len(content) - 1
    # Initializing the 'middle' with the middle value of first and last
    middle = (first + last) // 2

    # Continue the while loop till first<=last
    while (first <= last):
        # find the middle value in every iteration
        middle = (first + last) // 2
        # Checking whether s1 and the middle element are same or not
        # If they are same, we have foud the element
        if (s1 == content[middle]):
            print("Word found at ", middle)
            break
        # if s1 is greater than the middle element, then update the 'first' with 'middle+1' to see in the second half
        elif (s1 > content[middle]):
            first = middle + 1
        # if s1 is lesser than the middle element, then update the 'last' with 'middle-1' to see in the first half
        elif (s1 < content[middle]):
            last = middle - 1



def bubsort(list1):

    #Initializing content with list1
    content=list1

    #outer loop takes care of the number of iterations
    for i in content:
        #inner loop iterates from 1st element to the element just before the last element
        for j in range(0,len(content)-1):
            """comparing the two elements.
            If the first element is greater than the next element, then swap it"""
            if(content[j] > content[j+1]):
                temp=content[j]
                content[j]=content[j+1]
                content[j+1]=temp

    #returns the new list
    return content



def findnum(num):

    #Initializing n with num value
    n=num
    #(Initializing first with 0
    first=0
    #setting last as n-1
    last=n-1
    #Assigning the middle value of first and last to middle
    middle=(first+last)//2

    #Loop iterates till the condition holds true
    while(first<=last):

        #finding the mid element at each iteration
        middle=(first+last)//2

        print("The number is : ",middle)
        # Asking the user whether middle is the number or not
        a=int(input("Give 1 if this is the number ?"))

        #If That is the number, print thatb number
        if(a == 1):
            print("The number is : ",middle)
            break
        else:
            #If not, then confirm whether the number is greater than or less than this
            b=int(input("Give 1 If the number is greater than this ?"))
            """If it is greater, in the next iteration, only the second half will be considered
            If it is lesser ,only the first half will be considered"""
            if(b == 1):
                first=middle+1
                continue
            else:
                last=middle-1




def binarysearch(num, list2, e):
    # Assigning the passed list2,e, and num to list1,elem and n
    list1 = list2
    elem = e
    n = num

    # Sorting the elements before doing the binary search
    list1.sort()
    print("Elements after sorting : ", list1)

    # Initializing the first with 0 and last with n-1
    first = 0
    last = n - 1
    # Initializing mid with the mid value of first and last
    mid = (first + last) // 2

    # continue till first<=last
    while (first <= last):

        # Finding the mid in each iteration
        mid = (first + last) // 2

        # Checking whether the mid element and the required element are same or not. If same, we have found the element
        if (elem == list1[mid]):
            print("The element found at : ", mid)
            break
        # If the mid element is less than the element, then continue with the second half of the list
        elif (elem > list1[mid]):
            first = mid + 1
        # If the mid element is greater than the element, then continue with the first half of the list
        elif (elem < list1[mid]):
            last = mid - 1



def intbubble(num,list2):
    #Assigning the passed num and list2 to n and list1
    n=num
    list1=list2

    #for performing the operation till the list gets sorted as one element will be moved to the last i each iteration
    for i in list1:
        #Taking the index from 0 to n-2
        for j in range(0,n-1):
            #Checking whether an element is less than the element just before that
            #If so, swap those two
            if list1[j]>list1[j+1]:
                temp=list1[j]
                list1[j]=list1[j+1]
                list1[j+1]=temp
    #returning the sorted list
    return list1



def integerinsertion(num,list2):
    #Assigning the passed num and list2 to n and list1
    n=num
    list1=list2

    #printing the list before sorting
    print("Before Sorting : ")
    for i in list1:
        print(i)

    #from index 1 to n-1
    for i in range(1,n):
        #from index 0 to n-2
        for j in range(0,n-1):
            """Checking if an element is less than a the numbers before that number.
            if so, swap those two numbers """
            if(list1[j] > list1[i]):
                temp=list1[j]
                list1[j]=list1[i]
                list1[i]=temp
    #returning the sorted list
    return list1


def monthlypayment(p, y, r):
    # Assigning the passed p,y, and r to principle,year and rate
    principle = p
    year = y
    rate = r

    n = 12 * year
    r = rate / (12 * 100)
    payment = (principle * r) / (1 - pow(1 + r, -n))
    return round(payment)




def prime():

    #considering the numbers from 2 to 1000(as 1 is not a prime number)
    for i in range(2,1000):
        #considering only till the half of i as maximum probable division will be it's half(i/2)
        for j in range(1,int(i//2)+1):
            """checking whether i is divisible by any number in that range.
            If it is not divisible, then go inside if, or else go to else block
            If it is divisible by any of those numbers, then it is not a prime number.
                So, come out of the inner loop and continue with the outer loop"""
            if(i % j != 0 or j == 1):
                """check whether j has reached the half of i or not. 
                If so, then print i and continue with the outer loop """
                if(j == i//2):
                    print(i)
                    break
            else:
                break


def sqrt(num):
    # assigning the passed 'num' to c
    c = num
    # Storing value of c inside a temporary variable 't'
    t = c

    # finding the value for epsilon
    epsilon = 1e-15
    while abs(t - (c / t)) > epsilon * t:
        t = 0.5 * ((c / t) + t)

    # returning 't'
    return t





def stringbinary(num, list2, e):
    # Assigning the passed num,list2, and e to n,list1 and elem
    n = num
    list1 = list2
    elem = e

    # Sorting the list
    list1.sort()

    # Printing the list
    print(list1)

    # Initializing first with 0
    first = 0
    # Initializing last with n-1
    last = n - 1
    # Initializing mid with the middle value of first and last
    mid = (first + last) // 2

    # continue till first<=last
    while (first <= last):

        # finding the new mid value in each iteration
        mid = (first + last) // 2

        """Checking if the middle element is the element we are searching for.
        If so, we have found the element. print it and come out of the loop """
        if (elem == list1[mid]):
            print("The element found at : ", mid)
            break
        # If the element is greater than mid, then continue with the second half
        elif (elem > list1[mid]):
            first = mid + 1
        # If the element is lesser than mid, then continue with the first half
        elif (elem < list1[mid]):
            last = mid - 1




def strbubblesort(num,list2):
    n=num
    list1=list2
    #for performing the operation till the list gets sorted as one element will be moved to the last i each iteration
    for i in list1:
        #Taking the index from 0 to n-2
        for j in range(0,n-1):
            """Checking whether an element is less than the element just before that
            If so, swap those two """
            if list1[j]>list1[j+1]:
                temp=list1[j]
                list1[j]=list1[j+1]
                list1[j+1]=temp
    #returning the sorted list
    return list1





def stringinsertion(num,list2):
    #Assigning the passed num and list2 to n and list1
    n=num
    list1=list2

    #printing the list before sorting
    print("Before Sorting : ")
    for i in list1:
        print(i)

    #from index 1 to n-1
    for i in range(1,n):
        #from index 0 to n-2
        for j in range(0,n-1):
            """Checking if an element is less than a the numbers before that number.
            if so, swap those two numbers """
            if(list1[j] > list1[i]):
                temp=list1[j]
                list1[j]=list1[i]
                list1[i]=temp
    #returning the sorted list
    return list1





def swapnibble(num):
    # Assigning the passed num to 'n'
    n = num
    list1 = []

    # converting decimal number to binary and storing it into list1
    while (n != 0):
        n1 = n // 2
        r = n % 2
        list1.append(r)
        n = n1

    # Reversing the list
    list1.reverse()

    # Adds 0's to make it an 8 bit
    while (len(list1) != 8):
        list1.append(0)

    # printing the new list
    for i in list1:
        print(i)

    # swapping the first 4 elements with the last 4 elements
    for i in range(0, len(list1) // 2):
        temp = list1[i]
        list1[i] = list1[i + 4]
        list1[i + 4] = temp

    # rinting the list contents after swapping
    print("After Swapping : ")
    for i in list1:
        print(i)

    j = len(list1) - 1
    sum1 = 0
    i = 0

    # converting from binary to decimal
    while (j >= 0):
        sum1 = sum1 + pow(2, j) * list1[i]
        i += 1
        j -= 1
    return sum1




def tempconvert(num):
    # Assigning the passed num to 'n'
    n = num

    # convert from Celsius to Farenheit if n is 1
    if (n == 1):
        c1 = int(input("Enter the Temperature in Celsius:"))
        f1 = (c1 * (9 / 5)) + 32
        print("Temperature in Farenheit : ", f1)
    # convert from Farenheit to Celsius if n is 2
    elif (n == 2):
        f2 = int(input("Enter the temperature in Farenheit : "))
        c2 = (f2 - 32) * (5 / 9)
        print("Temperature in Celsius : ", c2)
    # Invalid input if the input is not 1 or 2
    else:
        print("Invalid Input.. Enter either 1 or 2")