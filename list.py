list=[]
total=0
n=int(input("enter the number of elements"))
for i in range(0,n):
    ele=int(input())
    list.append(ele)
print(list)
for i in list:
    total+=i
print(total)