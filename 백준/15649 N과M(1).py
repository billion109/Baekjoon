n,m = map(int,input().split(' '))
check = []
m_count = 0
x = []

def fun(chk, cnt):
    temp = cnt+1
    if temp<m:
        for i in range(n):
            if len(chk)>0:
                if i+1 < chk[-1]:
                    continue
            temp2 = chk[:]
            temp2.append(i+1)
            fun(temp2, temp)


    elif temp==m:
        for i in range(n):
            if len(chk)>0:
                if i+1 < chk[-1]:
                    continue
            temp2 = chk[:]
            temp2.append(i+1)
            for i in range(len(temp2)):
                if i==len(temp2)-1:
                    print(temp2[i])
                else:
                    print(temp2[i],end=' ')

    else:
        return

fun(check, m_count)

