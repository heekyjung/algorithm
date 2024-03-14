import sys
from collections import deque

# 정수 n (1 이상 10의 6승 이하)
n = int(sys.stdin.readline())

make1 = [0, 0]

if n >= 2:
    for i in range(2, n+1):
        before = make1[i-1]
        if i % 3 == 0 and make1[i//3] <= before:
            before = make1[i//3]
        if i % 2 == 0 and make1[i//2] <= before:
            before = make1[i//2]
        
        make1.append(before + 1)

print(make1[n])