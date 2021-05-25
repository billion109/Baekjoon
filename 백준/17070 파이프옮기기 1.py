import sys
input = sys.stdin.readline


def solution(n, house):



if __name__ == "__main__":
    n = int(input())
    house = [list(map(int, input().split())) for _ in range(n)]
    solution(n, house)
