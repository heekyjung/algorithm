import sys
import math
n = int(sys.stdin.readline())
a_list = list(map(int, sys.stdin.readline().split()))
b, c = map(int, sys.stdin.readline().split())

answer = 0
for a in a_list:
    left = a - b
    answer += 1
    if left > 0:
        sub = math.ceil(left / c)
        answer += sub
print(answer)