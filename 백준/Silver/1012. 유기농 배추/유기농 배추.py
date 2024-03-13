import sys
from collections import deque

# t : 테스트 케이스의 개수
t = int(sys.stdin.readline())

# 상하좌우 이동
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(coordinates):
    global worm

    x, y = coordinates
    # deque([[0, 0], [1, 0], [1, 1], [4, 2], [4, 3], [4, 5], [2, 4], [3, 4], [7, 4], [8, 4], [9, 4], [7, 5], [8, 5], [9, 5], [7, 6], [8, 6], [9, 6]])

    # 지렁이 침투! -> c_queue 에서는 빼주기!
    w_queue = deque([[x, y]])

    c_queue.popleft()
    # deque([[1, 0], [1, 1], [4, 2], [4, 3], [4, 5], [2, 4], [3, 4], [7, 4], [8, 4], [9, 4], [7, 5], [8, 5], [9, 5], [7, 6], [8, 6], [9, 6]])

    while w_queue:
        x, y = w_queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if [nx, ny] in c_queue:
                w_queue.append([nx, ny])
                c_queue.remove([nx, ny])
    worm += 1
    return worm

for _ in range(t):
    # m : 가로 길이, n : 세로 길이, k : 배추 위치의 개수
    m, n, k = map(int, sys.stdin.readline().split())

    # 배추 위치
    graph = list(list(map(int, sys.stdin.readline().split()))
                 for _ in range(k))
    # [[0, 0], [1, 0], [1, 1], [4, 2], [4, 3], [4, 5], [2, 4], [3, 4], [7, 4], [8, 4], [9, 4], [7, 5], [8, 5], [9, 5], [7, 6], [8, 6], [9, 6]]

    # 배추 위치도 큐로 해야지
    c_queue = deque(graph)

    worm = 0

    while c_queue:
        bfs(c_queue[0])
    print(worm)