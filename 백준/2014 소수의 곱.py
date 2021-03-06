import sys
import heapq

input = sys.stdin.readline

if __name__ == "__main__":
    K, N = map(int, input().split())
    prime = list(map(int, input().split()))
    q = prime[:]

    n = 0
    while True:
        #print(q)

        val = heapq.heappop(q)
        n += 1
        if n == N:
            print(val)
            break
        for i in prime:
            heapq.heappush(q, val * i)
            if val % i == 0:
                break


