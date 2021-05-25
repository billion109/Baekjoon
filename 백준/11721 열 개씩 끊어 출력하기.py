import sys
input = sys.stdin.readline


if __name__ == "__main__":
    str = input()
    str_len = len(str)
    cnt = str_len//10
    if str_len%10!=0:
        cnt+=1

    for i in range(cnt):
        if i != cnt-1:
            print(str[10*i:10*i+10])
        else:
            print(str[10*i:])

