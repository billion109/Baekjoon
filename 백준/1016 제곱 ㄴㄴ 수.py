import sys
import math

input = sys.stdin.readline

min_val, max_val = map(int, input().split())
square_numbers = []
ans = max_val - min_val + 1
numbers = set()

for i in range(2, max_val):
    if i ** 2 <= max_val:
        square_numbers.append(i ** 2)
    else:
        break

for square_number in square_numbers:
    i = math.ceil(min_val / square_number)
    while i * square_number <= max_val:
        numbers.add(i * square_number)
        i += 1

if 0 in numbers:
    numbers.discard(0)
print(ans - len(numbers))
