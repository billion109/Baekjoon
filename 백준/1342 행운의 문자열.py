s = input().rstrip()
ans = set()
def fun(c, string, curr):
    tmp = 0
    if len(string)==0:
        ans.add(curr)
    # print(c,string)
    for i in range(len(string)):
        if c == string[i]:
            continue
        else:
            fun(string[i], string[:i]+string[i+1:], curr+string[i])


for i in range(len(s)):

    fun(s[i], s[:i]+s[i+1:], s[i])

print(len(ans))