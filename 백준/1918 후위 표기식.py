import sys

input = sys.stdin.readline

if __name__ == "__main__":
    line = input().rstrip()
    ans = ''
    stack = []
    pos = 0
    for c in line:
        #print(c, stack, ans,type(c))
        if c == "(":
            stack.append(c)
        elif c == ")":
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.pop()
        elif c == "+" or c == "-":
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.append(c)
        elif c == "*" or c == "/":
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                ans += stack.pop()
            stack.append(c)
        else:
            ans += c

    while stack:
        ans += stack.pop()
    print(ans)

"""
A+B-C*D-C*(A+B)-D
"""
