from oopsprograms.stockreports_utility import Stockreports

#calling the file_open() function to open the json file and stores the data
json_string =Stockreports.file_open()
bool1="True"
while(bool1 == "True"):
    Stockreports.displaystock(json_string)
    print("1.Display")
    print("2.Buy")
    print("3.Sell")
    n=int(input("Select an option : "))
    if(n == 1):
        #Calls the display() method if the user has choosed '1'
        Stockreports.displaystock(json_string)
    elif(n == 2):
        # Calls the buystock() method and stores the data if the user has choosed '2'
        json_string=Stockreports.buystock(json_string)
        #Updates the data in the file with file_update() method
        Stockreports.file_update(json_string)
    elif(n == 3):
        # Calls the sellstock() method and stores the data if the user has choosed '3'
        json_string=Stockreports.sellstock(json_string)
    bool1=input("Do you want to continue : True or False")

        
    
