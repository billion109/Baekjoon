import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    ans = sys.maxsize
    val1, val2 = 0, 0

    for i in range(n-1):
        start = i+1
        end = n - 1

        while start <= end:
            mid = (start + end) // 2
            if arr[i]+arr[mid] < 0:
                start = mid + 1
            elif arr[i]+arr[mid] > 0:
                end = mid - 1
            else:
                ans = 0
                val1 = arr[i]
                val2 = arr[mid]
                break


        if ans == 0:
            break



        if mid != n-1:
            if abs(arr[mid]+arr[i]) < abs(arr[mid+1]+arr[i]):
                if abs(arr[mid]+arr[i]) < ans:
                    val1, val2 = arr[i], arr[mid]
                    ans = abs(arr[mid]+arr[i])
            else:
                if abs(arr[mid+1]+arr[i]) < ans:
                    val1,val2 = arr[i], arr[mid+1]
                    ans =abs(arr[mid+1]+arr[i])
        else:
            if abs(arr[mid] + arr[i]) < ans:
                val1, val2 = arr[i], arr[mid]
                ans = abs(arr[mid] + arr[i])

        print(i, start, end, mid, ans)


    print(ans)
    print(val1,val2)
