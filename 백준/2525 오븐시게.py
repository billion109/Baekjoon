h,m = map(int,input().split())
t = int(input())
ans = 60*h+m
ans+= t
ans = ans%1440
print(ans//60,ans%60)
