import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(adjacent, K):
    prev = [-1]*(len(adjacent))
    dist = [INF]*(len(adjacent))
    dist[K] = 0

    q = []
    heapq.heappush(q, [0, K])

    while q:
        curr_dist, curr_node = heapq.heappop(q)
        for next_node, weight in adjacent[curr_node].items():
            next_dist = curr_dist + weight
            if next_dist < dist[next_node]:
                dist[next_node] = next_dist
                prev[next_node] = curr_node
                heapq.heappush(q, [next_dist, next_node])
    return dist, prev




if __name__ == "__main__":
    V, E = map(int, input().split())
    K = int(input().rstrip())
    adjacent = [{} for _ in range(V + 1)]

    for i in range(E):
        u, v, w = map(int, input().split())
        if v in adjacent[u]:
            adjacent[u][v] = min(adjacent[u][v], w)
        else:
            adjacent[u][v] = w
    dist, prev = dijkstra(adjacent, K)

    for d in dist[1:]:
        if d == INF:
            print('INF')
        else:
            print(d)
