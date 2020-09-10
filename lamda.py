def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mydoubler1 = lambda a: a*a*a

print(mydoubler(11))
print(mydoubler1(3))