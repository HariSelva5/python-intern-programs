import json
with open("e:/python examples/python-intern-programs/Menu.json") as json_file:
    data=json.load(json_file)
    index=0
    for p in data['Starters']:
        print("gobi manchurian:"+p)
        ++index
       