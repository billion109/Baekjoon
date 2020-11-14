n,m = map(int,input().split())
arr = []
rbo = [[0,0],[0,0],[0,0]]

for i in range(n):
    x = list(input())
    for j in range(m):
        if x[j] == 'R':
            rbo[0] = [i,j]
        if x[j] == 'B':
            rbo[1] = [i, j]
        if x[j] == 'O':
            rbo[2] = [i,j]

def left(arr,rbo):
    if rbo[0][0] == rbo[1][0]: #R과B가 같은자리
        if rbo[0][1] < rbo[1][1]: #R이 왼쪽
            while arr[rbo[0][0] - 1][rbo[0][1]] == '.':
                rbo[0][0] -= 1
            if arr[rbo[0][0] - 1][rbo[0][1]] == 'O':  # R이 구멍에빠짐
                while arr[rbo[1][0] - 1][rbo[1][1]] == '.':
                    rbo[1][0] -= 1
                if arr[rbo[1][0] - 1][rbo[1][1]] == 'O':  # B가 구멍에빠짐
                    return -1   #R,B둘다 구멍에빠짐
                else:
                    return 1    #R만 구멍에빠짐
        else:   #R이 오른쪽
            pass
    else:   #R과B가 다른자리
        while arr[rbo[1][0]-1][rbo[1][1]]=='.':
            rbo[1][0]-=1
        if arr[rbo[1][0]-1][rbo[1][1]] == 'O':  #B가 구멍에빠짐
            return -1       #실패
        while arr[rbo[0][0]-1][rbo[0][1]]=='.':
            rbo[0][0] -=1
        if arr[rbo[0][0]-1][rbo[0][1]] == 'O':  #R이 구멍에빠짐
            return 1    #성공
        return 0 #계속
def right(arr,rbo):
    pass

def up(arr,rbo):
    pass

def down(arr,rbo):
    pass

print(arr)
print(rbo)