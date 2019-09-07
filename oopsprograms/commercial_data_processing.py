"""

    Name : commercial_data_processing.py
    Date : 31/08/2019
    Purpose : Commercial data processing

"""


from oopsprograms.commercialdataprocessing_utility import Commercial

#creating the object of the Commercial class
com=Commercial()

#calling file_open() function to open the file and storing the content of the file
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
    #if the user entered '1', call display() method
    if(op == 1):
        com.display(json_string)
    # if the user entered '2', call buy() method
    elif(op == 2):
        json_string=com.buy(json_string)
    # if the user entered '3', call sell() method
    elif(op == 3):
        json_string=com.sell(json_string)
    elif(op == 4):
        com.findvalue(json_string)
    t=int(input("Do you want to continue..? Press 1 to continue and any other number to exit"))
    com.file_update(json_string)