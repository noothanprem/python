"""

    Name : commercial_data_processing.py
    Date : 31/08/2019
    Purpose : Commercial data processing

"""


from oopsprograms.commercialdataprocessingmain import Commercial

#creating the object of the Commercial class
com=Commercial()

#calling file_open() function to open the file and storing the content of the file
json_string=com.file_open()
print(json_string)

while True:
    print("1.Display")
    print("2.Buy")
    print("3.Sell")
    print("4.Find value")
    op=0
    while True:
        try:
            op=int(input("Choose 1,2,3, or 4 : "))
            if(op < 1 or op > 4):
                print("Enter either 1,2,3,or 4 only ")
                continue
            break
        except ValueError:
            print("Enter either 1,2,3,or 4 only ")
            continue

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
    com.file_update(json_string)
    d=int(input("Do you want to continue(1) or exit(2) : "))
    if(d == 2):
        break
