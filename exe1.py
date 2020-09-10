import requests,json
r=requests.get('https://api.quotable.io/quotes?author=gandhi')
gandhi=r.json()
print(gandhi)
with open('gandhi.json', 'w') as f:
    json.dump(gandhi, f)
