input()
s = input()
r = 31
M = 1234567891
sum = 0
for i in range(len(s)):
    t = (ord(s[i])-96)
    sum += t*(r**i)
    sum = sum%M

print(sum)