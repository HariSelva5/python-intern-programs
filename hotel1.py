import json
with open("E:\python examples\python-intern-programs\hot.json") as json_file:
    data=json.load(json_file)
    def menu_card():
        for i in data["menu"]["veg starters"]:
            print("\n",i)
        print("------------------")
        for j in data["menu"]["non veg starters"]:
            print("\n",j)
        print("------------------")
        for k in data["menu"]["veg maindish"]:
            print("\n",k)
        print("------------------")
        for l in data["menu"]["non veg maindish"]:
            print("\n",l)
        print("------------------")
    menu_card()
    n=int(input("enter the no of items in veg starters:"))
    boughtvs=[]
    for i in range(n):
        i=str(input("enter item name:"))
        boughtvs.append(i)
    
    n=int(input("enter the no of items in  non veg starters:"))
    boughtns=[]
    for i in range(n):
        i=str(input("enter item name:"))
        boughtns.append(i)
    
    n=int(input("enter the no of items in  veg main dish:"))
    boughtvm=[]
    for i in range(n):
        i=str(input("enter item name:"))
        boughtvm.append(i)
    
    n=int(input("enter the no of items in  non veg maindish:"))
    boughtnm=[]
    for i in range(n):
        i=str(input("enter item name:"))
        boughtnm.append(i)
    
    cost=[]
    def _getPricevs(itemname):
        for vdishes in data["menu"]:
            if(vdishes=="veg starters"):
                if(data["menu"]["veg starters"][itemname]):
                    cost.append(data["menu"]["veg starters"][itemname])
                    return (data["menu"]["veg starters"][itemname])
                else:
                    continue
            else:
                continue

    def _getPricens(itemname):
        for ndishes in data["menu"]:
            if(ndishes=="non veg starters"):
                if(data["menu"]["non veg starters"][itemname]):
                    cost.append(data["menu"]["non veg starters"][itemname])
                    return (data["menu"]["non veg starters"][itemname])
                else:
                    continue
            else:
                continue

    def _getPricevm(itemname):
        for vmdishes in data["menu"]:
            if(vmdishes=="veg maindish"):
                if(data["menu"]["veg maindish"][itemname]):
                    cost.append(data["menu"]["veg maindish"][itemname])
                    return (data["menu"]["veg maindish"][itemname])
                else:
                    continue
            else:
                continue

    def _getPricenm(itemname):
        for nvmdishes in data["menu"]:
            if(nvmdishes=="non veg maindish"):
                if(data["menu"]["non veg maindish"][itemname]):
                    cost.append(data["menu"]["non veg maindish"][itemname])
                    return (data["menu"]["non veg maindish"][itemname])
                else:
                    continue
            else:
                continue

       
    for bitem in boughtvs:
        print(_getPricevs(bitem))
    for bitem in boughtns:
        print(_getPricens(bitem))
    for bitem in boughtvm:
        print(_getPricevm(bitem))
    for bitem in boughtnm:
        print(_getPricenm(bitem))
    
    print("The total bill is {}".format(sum(cost)))