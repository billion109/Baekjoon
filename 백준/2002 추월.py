import sys
from collections import defaultdict
from collections import deque

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    fr = [input().rstrip() for _ in range(n)]
    to = deque([input().rstrip() for _ in range(n)])
    check = defaultdict(int)
    ans = 0

    for car in fr:
        if check[car]>0:
            continue
        while to:
            car2 = to.popleft()
            if car == car2:
                break
            else:
                check[car2] += 1
                ans +=1

    print(ans)
