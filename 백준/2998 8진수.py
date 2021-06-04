import sys

input = sys.stdin.readline

if __name__ == "__main__":
    dic = {"000":0, "001":1, "010":2,
           "011":3, "100":4, "101":5,
           "110":6, "111":7}
    x = input().rstrip()
    if len(x) % 3 == 1:
        x = "00" + x
    elif len(x) % 3 == 2:
        x = "0" + x

    ans = ""
    for i in range(len(x) // 3):
        y = x[3 * i:3 * i + 3]
        ans+=str(dic[y])
    print(ans)
