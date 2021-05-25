import sys
from collections import defaultdict

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    cnt_dict = defaultdict(int)
    ans_dict = defaultdict(int)
    ans = 0
    for i in range(n):
        cnt_dict[str(arr[i])] += 1

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] == 0 and arr[j] != 0:
                if cnt_dict[str(arr[j])] < 2:
                    continue
            elif arr[i] !=0 and arr[j] == 0:
                if cnt_dict[str(arr[i])] < 2:
                    continue

            ans_dict[str(arr[i] + arr[j])] += 1

    for i in range(n):
        if arr[i] == 0:
            if cnt_dict['0']<=2:
                if ans_dict['0']>=cnt_dict['0']:
                    ans+=1
            else:
                ans+=1
        else:
            if ans_dict[str(arr[i])] > 0:
                ans += 1

    print(ans)
