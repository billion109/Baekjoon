import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(adjacent, K):
    dist = [INF]*len(adjacent)
    dist[K] = 0

    q = []
    heapq.heappush(q,[0,K])

    while q:
        curr_dist, curr_node = heapq.heappop(q)
        for next_node, weight in adjacent[curr_node].items():
            next_dist = curr_dist + weight
            if next_dist < dist[next_node]:
                dist[next_node] = next_dist
                heapq.heappush(q,[next_dist, next_node])
    return dist

if __name__ == "__main__":
    N = int(input())
    M = int(input())
    adjacent = [{} for _ in range(N+ 1)]
    for _ in range(M):
        fr, to, w = map(int, input().split())
        if to in adjacent[fr]:
            adjacent[fr][to] = min(adjacent[fr][to], w)
        else:
            adjacent[fr][to] = w

    start, end = map(int,input().split())

    dist = dijkstra(adjacent, start)
    print(dist[end])

