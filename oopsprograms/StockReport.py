import json
import datetime
# def displayShare():
#     print(dict1)
# def buyshare(num):
#     c=num
#     if(c == 1):
#         share_count1=int(dict1['Reliance']['share_count'])
#         print(share_count1)
#         if(share_count1 <= 0):
#             print("No more shares left")
#             return
#         else:
#             amount=int(input("Enter the amount"))
#             share_cost1=int(dict1['Reliance']['share_cost'])
#             if(amount > share_cost1):
#                 print("Enter the amount less than ",share_cost1)
#                 return
#             else:
#                 dict1['Reliance']['share_cost']=share_cost1-amount
#                 dict1['Reliance']['share_count']=share_count1-1
                
#     elif(c == 2):
#         if(dict1['ITC']['share_count'] <= 0):
#             print("No more shares left")
#             return
#         else:
#             amount=int(input("Enter the amount"))
#             if(amount > dict1['ITC']['share_cost']):
#                 print("Enter the amount less than ",dict1['ITC']['share_cost'])
#                 return
#             else:
#                 dict1['ITC']['share_cost']=dict1['ITC']['share_cost']-amount
#                 dict1['ITC']['share_count']-=1
#     elif(c == 3):
#         if(dict1['TATA']['share_count'] <= 0):
#             print("No more shares left")
#             return
#         else:
#             amount=int(input("Enter the amount"))
#             if(amount > dict1['TATA']['share_cost']):
#                 print("Enter the amount less than ",dict1['TATA']['share_cost'])
#                 return
#             else:
#                 dict1['TATA']['share_cost']=dict1['TATA']['share_cost']-amount
#                 dict1['TATA']['share_count']-=1


                

# with open('stock.json', 'r') as f:
#     content=f.readlines
#     dict1 = json.dumps(content)

# elif(n == 2):
#     print()
#     print("2.ITC")
#     print("3.TATA")
#     c=int(input("Choose the company :"))
#     buyshare(c)

def displayShare(json_string):
    for stock in range(len(json_string)):
        print("Name of the company :",json_string[stock]['name'])
        print("Shares of the company :",json_string[stock]['share_count'])
        print("Price  of the shares :",json_string[stock]['share_cost'])
        print()
temp_dict={ "name": None,
    "share_count" : None ,
    "share_cost" : None,
    "time" : None
    }
def buy(json_string):
    c_name=input ("enter the Company Name: ")
    for stock in range(len(json_string)):
        if json_string[stock]['name']==c_name:
            json_string[stock]['share_count']=int(input ("enter the shares :"))
            json_string[stock]['share_cost']=int(input ("enter the cost :"))
            return json_string
        else:
            temp_dict['name']=c_name
            c_name=None
            temp_dict['share_count']=input ("enter the shares :")
            temp_dict['share_cost']=input ("enter the cost :")
            temp_dict['time']=str(datetime.datetime.now())
            json_string.append(temp_dict)
            return json_string









if __name__ == "__main__":
    try:
        with open ('/home/admin81/Desktop/noothan/python/ObjectOrientedPrograms/new.json','r+') as f:
            content =f.read()
 
            json_string=json.loads(content)
         
    except FileNotFoundError as e:
        print(e)
    while(True):

        print("1.Display Share Details")
        print("2.Buy Share")
        print("3.Sell Share")
        n=int(input("Choose any one option :"))
  
        if(n == 1):
            displayShare(json_string)


        elif n== 2:

            json_string= buy(json_string)
            with open ('/home/admin81/Desktop/noothan/python/ObjectOrientedPrograms/new.json','r+') as f:
            
                json.dump(json_string,f)

        else:
            pass