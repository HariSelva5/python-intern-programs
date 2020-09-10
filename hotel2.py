import json
with open("E:\python examples\python-intern-programs\hot.json") as json_file:
    data=json.load(json_file)
    bought=[]
    n=int(input("enter the number of items:"))
    for i in range(n):
        i=str(input("enter item name:"))
        bought.append(i)
    def _getPrice(itemname):
        for m,n in data["menu"].items():
            for key,value in n.items():
                if (key==itemname):
                    return value

pricelist =[]       
for b in bought:
    if (_getPrice(b)!= None):
        pricelist.append(_getPrice(b))
sum=0
for i in pricelist:
    print(i)
    sum = sum + int(i)
print("Total Price :" + str(sum))


   