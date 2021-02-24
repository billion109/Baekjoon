import sys

input = sys.stdin.readline

N, M = map(int, input().split())
words = []
words_check = [True for _ in range(N)]
alphabet = 2 ** 26 - 1
base = 2 ** 26 - 1
count = N
for i in range(N):
    word = input().strip()
    word = ''.join(set(word))
    word = word.replace('a', '')
    word = word.replace('i', '')
    word = word.replace('e', '')
    word = word.replace('o', '')
    word = word.replace('u', '')

    temp = 0
    for c in word:
        shift_num = ord(c) - ord('a')
        temp |= 1 << shift_num
    words.append(temp)

for i in range(M):
    o, x = input().split()
    shift_num = ord(x) - ord('a')
    if o == '2':
        alphabet |= 1 << shift_num
    else:
        alphabet &= alphabet - 2 ** shift_num

    for j in range(len(words)):
        temp = 1 << shift_num
        if temp & words[j] == temp:
            if o == '1':
                if words_check[j]:
                    words_check[j] = False
                    count -= 1
            else:
                if words[j] & alphabet == words[j]:
                    words_check[j] = True
                    count += 1

    print(count)
