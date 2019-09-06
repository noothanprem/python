import json
import datetime
class Commercial:
    def file_open(self):
        with open("commercial.json","r") as f:
            content=f.read()
    
        json_string=json.loads(content)
        return json_string

    def file_update(self,json_string):
        with open("commercial.json","w") as f:
            json.dump(json_string,f)
        
    def display(self,json_string):
        print(json_string)
        i=0
        while(i < len(json_string)):
            print("Name of the company : ",json_string[i]["name"])
            print("Number of shares : ",json_string[i]["share_count"])
            print("Share Price : ",json_string[i]["share_price"])
            i+=1
    def findvalue(self,json_string):
        c_name=input("Enter the company name : ")
        len1=len(json_string)
        for i in range(len1):
            if(json_string[i]["name"] == c_name):
                print("value = ",int(json_string[i]["share_count"])*int(json_string[i]["share_price"]))
                return
        print("The Given company is not available")

    def buy(self,json_string):
        c_name=input("Enter the company name : ")
        len1=len(json_string)
        dict1={
            "name":None,
            "share_count":None,
            "share_price":None,
            "update_time":None
        }
        for i in range(len1):
            if(c_name == json_string[i]["name"]):
                json_string[i]["share_count"]=int(json_string[i]["share_count"]) + int(input("Enter the number of shares : "))
                json_string[i]["share_price"]=input("Enter the share price : ")
                json_string[i]["updated_time"]=str(datetime.datetime.now())
                return json_string
        dict1["name"]=c_name
        dict1["share_count"]=input("Enter the number of shares : ")
        dict1["share_price"]=input("Enter the share price : ")
        json_string.append(dict1)
        return json_string
    def sell(self,json_string):
        c_name=input("Enter the company name : ")
        len1=len(json_string)
        for i in range(len1):
            if(c_name == json_string[i]["name"]):
                shares=int(input("Enter the number of shares : "))
                if(shares > int(json_string[i]["share_count"])):
                    print("Only ",json_string[i]["share_count"]," shares left, Please Re enter")
                    return json_string
                json_string[i]["share_count"] = int(json_string[i]["share_count"]) - shares
                return json_string
        print("The Given company is not available")

                
if __name__ == "__main__":
    com=Commercial()
    json_string=com.file_open()
    print(json_string)
    print(type(json_string))
    t=1
    while(t == 1):
        print("1.Display")
        print("2.Buy")
        print("3.Sell")
        print("4.Find value")
        op=int(input("Choose 1,2,3, or 4 : "))
        if(op == 1):
            com.display(json_string)
        elif(op == 2):
            json_string=com.buy(json_string)
        elif(op == 3):
            json_string=com.sell(json_string)
        elif(op == 4):
            com.findvalue(json_string)
        t=int(input("Do you want to continue..? Press 1 to continue and any other number to exit"))
        com.file_update(json_string)