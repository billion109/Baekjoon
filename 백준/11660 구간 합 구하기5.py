import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        sum = 0
        temp = []
        for i in list(map(int, input().split())):
            sum += i
            temp.append(sum)
        arr.append(temp)
    # 누적합계산
    #print(arr)
    for _ in range(M):
        x1, y1, x2, y2 = map(int, input().split())
        ans = 0
        for i in range(x1 - 1, x2):
            ans += arr[i][y2 - 1]
            if y1 > 1:
                ans -= arr[i][y1 - 2]
        print(ans)
