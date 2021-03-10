import sys

input = sys.stdin.readline
INF = sys.maxsize

if __name__ == "__main__":
    T = int(input().rstrip())
    for _ in range(T):
        N, M, W = map(int, input().split())
        adjacent = [{} for _ in range(N + 1)]
        visited = [False] * (N + 1)
        for i in range(M):
            u, v, w = map(int, input().split())
            if v in adjacent[u]:
                adjacent[u][v] = min(adjacent[u][v], w)
            else:
                adjacent[u][v] = w

            if u in adjacent[v]:
                adjacent[v][u] = min(adjacent[v][u], w)
            else:
                adjacent[v][u] = w

        for i in range(W):
            u, v, w = map(int, input().split())
            w = -w
            if v in adjacent[u]:
                adjacent[u][v] = min(adjacent[u][v], w)
            else:
                adjacent[u][v] = w

        minus_cycle = False
        distance = [INF] * (N + 1)
        distance[1] = 0
        visited[0] = True
        visited[1] = True
        # 싸이클 검사를 위해 (N-1) + 1번 반복
        for i in range(N):
            for j in range(1, N + 1):
                for next, weight in adjacent[j].items():
                    #print(i, j, distance)
                    if distance[j] != INF and distance[next] > distance[j] + weight:
                        distance[next] = distance[j] + weight
                        visited[next] = True
                        # N번째 시행에서 값이 갱신되면 음의 싸이클이 존재
                        if i == N - 1:
                            minus_cycle = True

        # 1번에서 시작했기에, 분리되어 있는 컴포넌트는 싸이클 계산이 안됨.
        # 그렇기에 방문하지않은노드에서 재시작
        for i in range(1, N + 1):
            if not visited[i]:
                distance = [INF] * (N + 1)
                distance[i] = 0
                visited[i] = True
                for i in range(N):
                    for j in range(1, N + 1):
                        for next, weight in adjacent[j].items():
                            #print(i, j, distance)
                            if distance[j] != INF and distance[next] > distance[j] + weight:
                                distance[next] = distance[j] + weight
                                visited[next] = True
                                # N번째 시행에서 값이 갱신되면 음의 싸이클이 존재
                                if i == N - 1:
                                    minus_cycle = True

        if minus_cycle:
            print("YES")
        else:
            print("NO")
