import json
with open("inventory.json","r") as f1:
    data = json.load(f1)
print(data)
print(type(data))
weight1=data['Rice']['weight']
print(weight1)
price1=data['Rice']['price']
w1=weight1.replace('Kg','')
weight2=data['Wheat']['weight']
price2=data['Wheat']['price']
w2=weight2.replace('kg','')
weight3=data['Pulses']['weight']
price3=data['Pulses']['price']
w3=weight3.replace('kg','')
print("Rice Total amount : ",int(w1)*int(price1))
print("Wheat Total amount : ",int(w2)*int(price2))
print("Pulses Total amount : ",int(w3)*int(price3))
