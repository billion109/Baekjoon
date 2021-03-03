import sys

sys.setrecursionlimit(5000)
input = sys.stdin.readline
ans = 0


def is_available(candidate, i):
    row = len(candidate)
    col = i
    for q_row in range(row):
        q_col = candidate[q_row]
        if abs(row - q_row) == abs(col - q_col):
            return False
    return True


def dfs(n, row, candidate):
    global ans
    if row == n:
        ans += 1
        return

    for i in range(n):
        if i in candidate:
            continue
        if is_available(candidate, i):
            candidate.append(i)
            dfs(n, row + 1, candidate)
            candidate.pop()


if __name__ == "__main__":
    n = int(input())

    dfs(n, 0, [])
    print(ans)
