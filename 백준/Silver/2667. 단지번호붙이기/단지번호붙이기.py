import sys
from collections import deque
# sys.stdin = open("sample_input.txt", "r")
n = int(sys.stdin.readline())
graph = list(list(map(int, sys.stdin.readline().strip())) for _ in range(n))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

blocks = []

def bfs(x, y):
    queue = deque([(x, y)])
    graph[x][y] = "V"
    count = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = "V"
                    queue.append((nx, ny))
                    count += 1
    return count

for r in range(n):
    for c in range(n):
        if graph[r][c] == 1:
            blocks.append(bfs(r, c))

blocks.sort()
print(len(blocks))
for b in blocks:
    print(b)