from itertools import combinations_with_replacement as comb
num = [1,5,10,50]
n = int(input())
print(len(set(map(sum,(comb(num,n))))))