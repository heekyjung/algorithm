import sys
from collections import deque

# m : 상자 가로 칸의 수, n : 상자 세로 칸의 수
m, n = map(int, sys.stdin.readline().split())

# 토마토 정보 받기
graph = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))

# [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1]]

# 나만의 x, y 좌표는 이번엔 이렇게!
# (0,0), (0,1), (0,2), ...
# (1,0), (1,1), (1,2), ...

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(queue):
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    queue.append((nx, ny))
                    graph[nx][ny] = graph[x][y] + 1

    day = float("-inf")  # 음의 무한
    for g in graph:
        if 0 in g:
            return -1
        if max(g) > day:
            day = max(g)
    return day - 1


tomato = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            tomato.append((i, j))

print(bfs(tomato))
