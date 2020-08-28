a=int(input("enter a value\n"))
b=int(input("enter b value\n"))
if((a and b)!= 0):
    if(isinstance(a,int)):
        a=float(a)
        print(a)
    else:
        print("something went wrong")
else:
    print("a,b values are zero")
