import sys
input = sys.stdin.readline
INF = sys.maxsize


if __name__ == "__main__":
    n = int(input().rstrip())
    m = int(input().rstrip())

    distance = []
    for i in range(n+1):
        temp = []
        for j in range(n+1):
            if i == j:
                temp.append(0)
            else:
                temp.append(INF)
        distance.append(temp)

    for _ in range(m):
        u,v,w = map(int,input().split())
        distance[u][v] = min(w, distance[u][v])

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])

    for i in range(1,n+1):
        for j in range(1,n+1):
            if distance[i][j] == INF:
                print(0,end=' ')
            else:
                print(distance[i][j],end=' ')
        print()

