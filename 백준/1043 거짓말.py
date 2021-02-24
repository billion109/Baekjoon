import sys

input = sys.stdin.readline

N, M = map(int, input().split())
temp = list(map(int, input().split()))
truth_num = temp[0]
if truth_num != 0:
    truth_numbers = temp[1:]
else:
    truth_numbers = []

parties = []
for i in range(M):
    parties.append(list(map(int, input().split())))

print(truth_numbers)
print(parties)