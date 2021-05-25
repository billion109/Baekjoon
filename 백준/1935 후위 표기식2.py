import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    post = input().rstrip()
    stack = []
    arr = [int(input()) for x in range(N)]

    for i in range(len(post)):
        # print(stack)
        if post[i] == "+":
            b = stack.pop()
            a = stack.pop()
            stack.append(a+b)
        elif post[i] == "-":
            b = stack.pop()
            a = stack.pop()
            stack.append(a - b)
        elif post[i] == "*":
            b = stack.pop()
            a = stack.pop()
            stack.append(a * b)
        elif post[i] == "/":
            b = stack.pop()
            a = stack.pop()
            stack.append(a / b)
        else:
            stack.append(arr[ord(post[i])-65])

    print("{:.2f}".format(stack[0]))