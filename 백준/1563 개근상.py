import sys

input = sys.stdin.readline

if __name__ == "__main__":
    dp1 = [1]  # No 지각, 0결석
    dp2 = [1]  # No 지각, 1결석
    dp3 = [0]  # No 지각, 2결석
    dp4 = [1]  # Yes 지각, 0결석
    dp5 = [0]  # Yes 지각, 1결석
    dp6 = [0]  # Yes 지각, 2결석

    n = int(input())
    for i in range(n):
        dp1.append((dp1[i] + dp2[i] + dp3[i])%1000000)
        dp2.append(dp1[i])
        dp3.append(dp2[i])
        dp4.append((dp1[i] + dp2[i] + dp3[i] + dp4[i] + dp5[i] + dp6[i])%1000000)
        dp5.append(dp4[i])
        dp6.append(dp5[i])

    print(dp4[-1])

