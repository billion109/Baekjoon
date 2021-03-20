n = int(input())
k = int(input())


def count(v):
    ans = 0
    for i in range(1, n + 1):
        ans += min(n, (v // i))

    return ans


def main():
    start = 1
    end = k
    while start <= end:
        mid = (start + end) // 2
        temp = count(mid)
        #print(start, end, mid, temp)
        if temp < k:
            start = mid + 1
        else:
            ret = mid
            end = mid - 1

    print(ret)


if __name__ == "__main__":
    main()
