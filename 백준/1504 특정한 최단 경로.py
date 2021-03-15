import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize


def dijkstra(n):
    distance = [INF] * (N + 1)
    distance[n] = 0
    priority_q = []
    heapq.heappush(priority_q, [0, n])

    while priority_q:
        curr_dist, curr_node = heapq.heappop(priority_q)
        for next_node, weight in adjacent[curr_node].items():
            if curr_dist + weight < distance[next_node]:
                distance[next_node] = curr_dist + weight
                heapq.heappush(priority_q, [distance[next_node], next_node])
    return distance


if __name__ == "__main__":
    N, E = map(int, input().split())
    adjacent = [{} for _ in range(N + 1)]
    for i in range(E):
        u, v, w = map(int, input().split())
        if v in adjacent[u]:
            adjacent[u][v] = min(adjacent[u][v], w)
            adjacent[v][u] = adjacent[u][v]
        else:
            adjacent[u][v] = w
            adjacent[v][u] = w

    v1, v2 = map(int, input().split())
    node_1 = dijkstra(1)
    node_N = dijkstra(N)
    node_v1 = dijkstra(v1)

    case1 = node_1[v1] + node_v1[v2] + node_N[v2]
    case2 = node_1[v2] + node_v1[v2] + node_N[v1]
    if case1 >= INF and case2 >= INF:
        print(-1)
    else:
        print(min(case1, case2))
