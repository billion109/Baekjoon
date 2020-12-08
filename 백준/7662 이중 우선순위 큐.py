import heapq
import sys
input = sys.stdin.readline

T = int(input())
visited = [0]*1000000


for i in range(T):
    k = int(input())
    highq = []
    lowq = []
    for j in range(k):
        op, num = input().split()
        num = int(num)
        if op == 'I':
            heapq.heappush(highq, (-num,j))
            heapq.heappush(lowq, (num,j))
            visited[j] = 1
        else:
            if num==1:
                while highq and visited[highq[0][1]]==0:
                    heapq.heappop(highq)
                if highq:
                    visited[highq[0][1]]=0
                    heapq.heappop(highq)
            else:
                while lowq and visited[lowq[0][1]] == 0:
                    heapq.heappop(lowq)
                if lowq:
                    visited[lowq[0][1]] = 0
                    heapq.heappop(lowq)


    while highq and visited[highq[0][1]]==0:
        heapq.heappop(highq)
    while lowq and visited[lowq[0][1]] == 0:
        heapq.heappop(lowq)
                    
    if highq:
        print(-highq[0][0], lowq[0][0])
    else:
        print('EMPTY')
