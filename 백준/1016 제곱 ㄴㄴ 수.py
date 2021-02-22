import sys
import math

input = sys.stdin.readline

min_val, max_val = map(int, input().split())

square_board = []
num_board = []

for i in range(2, math.ceil(math.sqrt(max_val))):
    square_board.append(i*i)

for i in range(num_board):
    print(square_board)