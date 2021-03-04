import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize


def dijkstra(adjacent, X):
    dist = [INF] * len(adjacent)
    dist[X] = 0

    q = []
    heapq.heappush(q, [0, X])

    while q:
        curr_dist, curr_node = heapq.heappop(q)
        for next_node, weight in adjacent[curr_node].items():
            next_dist = curr_dist + weight
            if next_dist < dist[next_node]:
                dist[next_node] = next_dist
                heapq.heappush(q, [next_dist, next_node])
    return dist


if __name__ == "__main__":
    N, M, X = map(int, input().split())
    # adjacent1은 정방향
    # adjacent2는 역방향
    adjacent1 = [{} for _ in range(N + 1)]
    adjacent2 = [{} for _ in range(N + 1)]
    for _ in range(M):
        u, v, w = map(int, input().split())
        if v in adjacent1[u]:
            adjacent1[u][v] = min(w, adjacent1[u][v])
        else:
            adjacent1[u][v] = w

        u, v = v, u
        if v in adjacent2[u]:
            adjacent2[u][v] = min(w, adjacent2[u][v])
        else:
            adjacent2[u][v] = w

    dist1 = dijkstra(adjacent1, X)
    dist2 = dijkstra(adjacent2, X)
    print(max([dist1[i]+dist2[i] for i in range(1,N+1)]))
