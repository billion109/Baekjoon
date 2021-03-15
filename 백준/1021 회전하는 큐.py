import sys
from collections import deque

input = sys.stdin.readline

if __name__ == "__main__":

    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    deck = deque([x for x in range(1, N + 1)])
    ans = 0
    for i in arr:
        index = deck.index(i)
        if index <= len(deck) // 2:
            deck.rotate(-index)
            ans += index
        else:
            deck.rotate(len(deck)-index)
            ans += len(deck)-index
        deck.popleft()
    print(ans)
