from collections import defaultdict

n = int(input())
n_list = list(map(int,input().split()))
m = int(input())
m_list = list(map(int,input().split()))

n_dic = defaultdict(int)
for i in n_list:
    n_dic[i]+=1

for i in m_list:
    print(n_dic[i],end=' ')