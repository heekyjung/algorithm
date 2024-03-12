from collections import deque

n = int(input()) # n장의 카드 (1~n)

queue = deque([i for i in range(1, n+1)])

# n = 4 이면, queue = deque([1, 2, 3, 4])

def card2():
    while len(queue) > 1:
        queue.popleft()
        pick = queue.popleft()
        queue.append(pick)
    print(queue[0])

card2()