import sys

input = sys.stdin.readline
from collections import deque
from collections import defaultdict


def reverse(string, start, k):
    s = string[start:start + k]
    new_string = string[:start] + s[::-1] + string[start + k:]
    return new_string


if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = input().rstrip()
    ans = list(map(int, arr.split()))
    ans.sort()
    ans = "".join(map(str, ans))
    arr = arr.replace(" ", "")
    check = defaultdict(int)
    q = deque()
    q.append([arr, 0])
    check[int(arr)] +=1
    while q:
        # print(q)
        string, cnt = q.popleft()
        if string == ans:
            print(cnt)
            break
        for start in range(0, n - k + 1):
            new_string = reverse(string, start, k)
            # print(new_string)
            if check[int(new_string)] == 0:
                q.append([new_string, cnt + 1])
                check[int(new_string)] +=1

    if string != ans:
        print(-1)


