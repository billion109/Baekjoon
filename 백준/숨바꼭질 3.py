import sys
from collections import deque

input = sys.stdin.readline

if __name__ == "__main__":
    n, k = map(int, input().split())
    deck = deque([])

    check = [True] * 100001
    check[n] = False
    deck.append([n, 0])
    while True:
        curr_pos, cnt = deck.popleft()
        if curr_pos == k:
            print(cnt)
            break
        elif curr_pos > k:
            if curr_pos > 0 and check[curr_pos - 1]:
                check[curr_pos - 1] = False
                deck.append([curr_pos - 1, cnt + 1])
        else:
            if curr_pos * 2 <= 100000 and check[curr_pos * 2]:
                check[curr_pos * 2] = True
                deck.appendleft([curr_pos * 2, cnt])
            if curr_pos > 0 and check[curr_pos - 1]:
                check[curr_pos - 1] = False
                deck.append([curr_pos - 1, cnt + 1])
            if curr_pos + 1 <= 100000 and check[curr_pos + 1]:
                check[curr_pos + 1] = False
                deck.append([curr_pos + 1, cnt + 1])
