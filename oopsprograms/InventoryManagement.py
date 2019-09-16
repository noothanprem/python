"""

    Name : InventoryManagement.py
    Date : 31/08/2019
    Purpose : To Create a JSON file having Inventory Details for Rice, Pulses and Wheats
              with properties name, weight, price per kg, read in JSON File and output thejson string

"""


from oopsprograms.inventorymanagementmain import Inventory


i1=Inventory()
#calling the function to find the value and display it
data=i1.file_open()
i1.find(data)