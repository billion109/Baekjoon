import sys


def is_palindrome(x):
    start = 0
    end = len(x) - 1
    while start <= end:
        if x[start] != x[end]:
            return False
        start += 1
        end -= 1
    return True


if __name__ == "__main__":
    string = input()
    length = len(string)
    dp = [2500] * (length + 1)
    dp[0] = 0
    # 여기서는 함수로 계속 팰린드롬을 확인하지만, 한번에 2차원으로
    # 팰린드롬테이블을 만든어서 확인한다면 시간복잡도가 줄어들것.
    for i in range(length + 1):
        for j in reversed(range(0, i)):
            if is_palindrome(string[j:i]):
                dp[i] = min(1 + dp[j], dp[i])

    print(dp[-1])
