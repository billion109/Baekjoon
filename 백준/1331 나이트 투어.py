def is_can_go(a, b):
    path = [[-2,-1],[-1,-2],[-2,1],[-1,2],[1,-2],[1,2],[2,-1],[2,1]]
    if [a[0]-b[0],a[1]-b[1]] in path:
        return True
    else:
        return False


def convert(str):
    pos_x = int(ord(str[0]) - 65)
    pos_y = int(str[1]) - 1
    return (pos_x, pos_y)


check = [[False] * 6 for _ in range(6)]
curr = convert(input())
first = curr
check[curr[0]][curr[1]] = True

for _ in range(35):
    next = convert(input())
    if is_can_go(curr, next):
        if check[next[0]][next[1]]:
            break
        else:
            check[next[0]][next[1]] = True
            curr = next
    else:
        break

for i in range(36):
    if not check[i//6][i%6]:
        print('Invalid')
        exit(0)
if is_can_go(first,curr):
    print("Valid")
else:
    print("Invalid")
