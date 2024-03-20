import sys
from collections import deque
# sys.stdin = open("sample_input.txt", "r")

# 세로 길이 n, 가로 길이 m, 음식물 쓰레기 개수 k
n, m, k = map(int, sys.stdin.readline().split())
graph = [[0] * m for _ in range(n)]

for _ in range(k):
    x, y = map(int, sys.stdin.readline().split())
    x, y = x-1, y-1
    graph[x][y] = 1
# graph = [[1, 0, 0, 0], [0, 1, 1, 0], [1, 1, 0, 0]]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

size = 0

def bfs(x, y):
    queue = deque([(x, y)])
    graph[x][y] = 2 # 방문한 곳은 2로 바꿈
    count = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    queue.append((nx, ny))
                    graph[nx][ny] = 2
                    count += 1
    return count

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            size = max(bfs(i, j), size)

print(size)