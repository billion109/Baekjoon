h,m,s = map(int,input().split())
t = int(input())
ans = 60*60*h+m*60+s
ans+= t
ans = ans%(60*60*24)
print(ans//3600,(ans%3600)//60, ans%60)
