import sys
from collections import deque

# 테스트 케이스의 개수 t
t = int(sys.stdin.readline())

cases = [0, 1, 2, 4]
for i in range(4, 11):
    cases.append(cases[i-1] + cases[i-2] + cases[i-3])

for _ in range(t):
    # 정수 n 은 양수이며, 11보다 작음
    n = int(sys.stdin.readline())

    print(cases[n])