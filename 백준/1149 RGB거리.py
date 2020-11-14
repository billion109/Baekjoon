def min_select(x,y,z):
    min_val = min(x,y,z)
    if min_val == x:
        return 1
    elif min_val == y:
        return 2
    elif min_val == z:
        return 3
    else:
        return -1

def min_repeat(x,y,z,num):
    if num==1:
        if y<=z:
            return 2
        else:
            return 3
    elif num ==2:
        if x<=z:
            return 1
        else:
            return 3
    elif num==3:
        if y<=z:
            return 2
        else:
            return 3




n = int(input())
arr = []
dp = [0]*n
dp_choice = [0]*n

for i in range(n):
    arr.append(list(map(int, input().split())))

dp[0] = min(arr[0][0], arr[0][1], arr[0][2])
dp_choice[0] = min_select(arr[0][0], arr[0][1], arr[0][2])
#r == 1, g==2, b==3


for i in range(1,n):
    min_val = min(arr[i][0], arr[i][1], arr[i][2])
    dp_choice[i] = min_select(arr[i][0], arr[i][1], arr[i][2])
    dp[i] = arr[i][dp_choice[i]-1]
    if dp_choice[i]==dp_choice[i-1]:
        dp_choice[i]=min_repeat(arr[i][0], arr[i][1], arr[i][2],dp_choice[i])
        dp[i] = arr[i][dp_choice[i] - 1]
    temp1 = dp[i]+dp[i-1]
#일단 겹치지않게 저장하는것까지함. 이제 dp비교하는거 해서 바꾸는거짜면됨. 아마 함수로만들어서 짜야할듯


print(dp)
print(dp_choice)

