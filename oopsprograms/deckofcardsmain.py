import random
class Deck:

    def find():

        #storing the ranks and faces in different lists
        rank=["2","3","4","5","6","7","8","9","10","jack","queen","king","ace"]
        face=["clubs","diamonds","hearts","spades",]

        #creating a list
        list1=[]

        #creating a string
        str1=''

        #Iterates through all the elements in the face list
        for i in face:
            # Iterates through all the elements in the rank list
            for j in rank:
                #making the string empty in each iteration
                str1=''
                #Appending elements of both face list and rank list each time
                str1+=i
                str1+=" : "
                str1+=j
                #Appending the string to the list in each iteration
                list1.append(str1)
        print("Before Shuffling : ",list1)
        random.shuffle(list1)
        print("After Shuffling : ",list1)
        i=0

        #Initializing 'count' with '0'
        count=0
        per1=[]
        per2=[]
        per3=[]
        per4=[]
        persons=[]
        #for i in range(36):
            #if i % 4 == 0:
                #print()
            #print(list1[i],end=' \t\t ')

        #For 4 Players
        while(i < 4):
             count=0
             #Iterates through the elements of list1
             for j in range(len(list1)):
                 #Break once we reach 9 cards
                 if(count == 9):
                     break
                 #Append to the 1st person's list
                 if(i == 0):
                     per1.append(list1[j])
                 # Append to the 2nd person's list
                 elif(i == 1):
                     per2.append(list1[j])
                 # Append to the 3rd person's list
                 elif(i == 2):
                     per3.append(list1[j])
                 # Append to the 1st person's list
                 elif(i == 3):
                     per4.append(list1[j])
                 #delete the element from list1
                 list1.pop(j)
                 count+=1
             i+=1

        #Appending all the persons list to a single list
        persons.append(per1)
        persons.append(per2)
        persons.append(per3)
        persons.append(per4)

        #printing the final list
        for item in persons:
            print(item)
