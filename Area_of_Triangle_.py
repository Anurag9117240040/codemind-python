import math as m
a,b,c=map(int,input().split())
s=(a+b+c)/2
area=s*(s-a)*(s-b)*(s-c)
area=m.sqrt(area)
print("%0.2f" % area)