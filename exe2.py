import requests,json
r=requests.get('https://api.quotable.io/quotes?tags=wisdom,famous-quotes')
wisdom=r.json()
print(wisdom)
with open('wisdom.json', 'w') as f:
    json.dump(wisdom, f)
    print(len(wisdom["results"]))
    
    