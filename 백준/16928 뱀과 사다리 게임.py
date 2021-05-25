import sys
from collections import deque

input = sys.stdin.readline
INF = sys.maxsize

if __name__ == "__main__":
    N, M = map(int, input().split())
    jump = []
    jump_fr = []
    nodes = [[] for i in range(101)]
    check = [True] * 101
    q = deque()

    for i in range(N + M):
        fr, to = map(int, input().split())
        jump.append([fr, to])
        jump_fr.append(fr)

    for i in range(1, 100):
        if i in jump_fr:
            fr, to = jump.pop(0)
            nodes[fr].append(to)

        else:
            for j in range(1, 7):
                if i + j <= 100:
                    nodes[i].append(i + j)

    # print(nodes)
    q.append([1, 0])
    check[1] = False
    while q:
        # print(q)
        curr, cnt = q.popleft()
        if curr == 100:
            print(cnt)
            break

        if nodes[curr]:
            for next in nodes[curr]:
                if check[next]:
                    check[next] = False
                    if next in jump_fr:
                        q.appendleft([next, cnt])
                    else:
                        q.append([next, cnt+1])

