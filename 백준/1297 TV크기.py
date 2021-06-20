import math
d,a,b = map(int,input().split())
c = math.sqrt(a**2+b**2)
print(int(d*a//c),int(d*b//c))
