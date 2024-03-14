import sys
from collections import deque

n = int(sys.stdin.readline())

def fib(num):
    f = [0, 1]
    
    if num == 1:
        return f[1]
    
    for i in range(1, num):
        f.append(f[i] + f[i-1])

    return f[num]

print(fib(n))