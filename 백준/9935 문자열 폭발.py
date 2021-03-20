import sys
from collections import deque

input = sys.stdin.readline


def compare(stack, bomb):
    if len(stack) < len(bomb):
        return

    temp = deque([])
    for i in reversed(bomb):
        temp2 = stack.pop()
        if temp2 == i:
            temp.append(temp2)
        else:
            stack.append(temp2)
            while temp:
                stack.append(temp.pop())
            return

    return


if __name__ == "__main__":
    string = input().rstrip()
    bomb = deque(list(input().rstrip()))
    stack = deque([])
    for i in string:
        stack.append(i)
        compare(stack, bomb)

    if stack:
        print("".join(map(str, stack)))
    else:
        print('FRULA')
