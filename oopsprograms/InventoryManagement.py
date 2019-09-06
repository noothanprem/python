import json
with open("inventory.json","r") as f:
    data=json.load(f)



for i in data:
    print(i)
    print(i, data[i]["name"], data[i]["weight"]* data[i]["price"])# ,int(data[0]['name']["weight"])*int(data[0]['name']["price"]))


# print("Price of Basmati Rice : ",int(data["rice"]["weight"])*int(data["rice"]["price"]))
# print("Price of Beans : ",int(data["pulses"]["weight"])*int(data["pulses"]["price"]))
# print("Price of Spelt : ",int(data["wheats"]["weight"])*int(data["wheats"]["price"]))

