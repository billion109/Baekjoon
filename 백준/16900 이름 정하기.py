import sys

input = sys.stdin.readline



if __name__ == "__main__":
    s, k = input().split()
    val = 0
    for i in range(1, len(s)):
        if s[:i] == s[-i:]:
            val = i

    left = len(s) - val
    ans = len(s)+left*(int(k)-1)

    print(ans)
