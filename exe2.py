import requests,json
r=requests.get('https://api.quotable.io/quotes?tags=wisdom,famous-quotes')
gandhio=r.json()
print(gandhio)
with open('gandhio.json', 'w') as f:
    json.dump(gandhio, f)
resjson = r.json()
icount = 0
listAuthor=[]
for i in resjson['results']:
    icount+=1
    listAuthor.append(i['author'])
print(icount)
listAuthor = list(dict.fromkeys(listAuthor))
for a in listAuthor:
    print(a)

    