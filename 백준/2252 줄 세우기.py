import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split())
    adjacent = [{} for _ in range(N + 1)]
    prev = [{} for _ in range(N + 1)]
    for _ in range(M):
        u, v = map(int, input().split())
        adjacent[u][v] = 1
        prev[v][u] = 1

