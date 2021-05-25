import sys

input = sys.stdin.readline

if __name__ == "__main__":
    L, R = input().split()
    ans = 0
    if len(L) == len(R):
        while len(L) >0:
            if L[0] == R[0]:
                if L[0] =="8":
                    ans += 1
                L = L[1:]
                R = R[1:]
            else:
                break

    print(ans)




