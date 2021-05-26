import sys
import heapq

INF = sys.maxsize
input = sys.stdin.readline

if __name__ == "__main__":
    n, m, r = map(int, input().split())
    items = list(map(int, input().split()))
    edges = [{} for i in range(n + 1)]
    ans = 0
    for i in range(r):
        u, v, w = map(int, input().split())
        if v in edges[u]:
            edges[u][v] = min(edges[u][v], w)
        else:
            edges[u][v] = w

        if u in edges[v]:
            edges[v][u] = min(edges[v][u], w)
        else:
            edges[v][u] = w

    for start_node in range(1, n + 1):
        curr_ans = 0
        distance = [INF] * (n + 1)
        distance[start_node] = 0
        q = []
        heapq.heappush(q, [0, start_node])

        while q:
            curr_dis, curr_node = heapq.heappop(q)
            for next_node, weight in edges[curr_node].items():
                next_dis = curr_dis + weight
                if next_dis < distance[next_node]:
                    distance[next_node] = next_dis
                    heapq.heappush(q, [next_dis, next_node])

        for i in range(1, n + 1):
            if distance[i] <= m:
                curr_ans += items[i - 1]

        # print(distance, curr_ans)

        ans = max(curr_ans, ans)
    print(ans)
