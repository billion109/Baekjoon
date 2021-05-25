import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5)


def bfs(i):
    check[i] = False
    if node[i]:
        for next in node[i]:
            if check[next]:
                val[i] += bfs(next)
            else:
                val[i] += val[next]

    else:
        return 1

    return val[i]


if __name__ == "__main__":
    N, M = map(int, input().split())
    node = [[] for _ in range(N + 1)]

    for i in range(M):
        u, v = map(int, input().split())
        node[v].append(u)

    check = [True] * (N + 1)
    val = [1] * (N + 1)

    for i in range(1, N + 1):
        if check[i]:
            bfs(i)

    print(*list(filter(lambda x: val[x] == max(val), range(len(val)))))
