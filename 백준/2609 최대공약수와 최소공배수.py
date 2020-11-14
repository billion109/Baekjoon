n,m = map(int,input().split())
if m>n:
    n,m = m,n

a,b = n,m
while b!=0:
    r = a%b
    a = b
    b = r

gcd = a
lcm = n*m/gcd

print(gcd)
print(int(lcm))