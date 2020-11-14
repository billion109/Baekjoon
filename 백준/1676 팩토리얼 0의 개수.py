N = int(input())
ans = 0
n=1
while 5**n<=N:
   ans+=N//(5**n)
   n+=1
print(ans)
