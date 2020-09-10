import json
with open("E:\python examples\python-intern-programs\hot.json") as json_file:
    data=json.load(json_file)
    bought=["paneer roll","veg roll"]
    # print(data["menu"]["veg starters"])
    def _getPrice(itemname):
        for m,n in data["menu"].items():
            for key,value in n.items():
                print(value)
    _getPrice("paneer roll")          
            
            # if(data["menu"]["veg starters"][itemname]!=None):
            #     return (data["menu"]["veg starters"][itemname])
        #    if (m[itemname]!=None):
        #        return m[itemname]
        # for m in data["menu"]["non veg starters"]:
        #    if (m[itemname]!=None):
        #        return m[itemname]
        # for m in data["menu"]["veg maindish"]:
        #    if (m[itemname]!=None):
        #        return m[itemname]
        # for m in data["menu"]["non veg maindish"]:
        #    if (m[itemname]!=None):
        #        return m[itemname]
    # for bitem in bought:
    #     print(_getPrice(bitem))

    # def add(a,b):
    #     c=a+b
    #     return(c)
    # j=add(3,4)
    # print(j)