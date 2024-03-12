import sys
from collections import deque

# 전쟁터의 가로 크기 n, 세로 크기 m (1~100 사이 정수)
n, m = map(int, sys.stdin.readline().split())  # 5, 5
graph = list(list(sys.stdin.readline().strip()) for _ in range(m))
# 요로코롬 들어온다 [['W', 'B', 'W', 'W', 'W'], ... , ['W', 'W', 'W', 'W', 'W']]
# W : 우리 병사 / B : 적국 병사

# 상하좌우 탐색을 위한 이동 표시
dx = [-1, 1, 0, 0]  # 상하좌우 이동 시 x 값이 바뀌는 정도
dy = [0, 0, -1, 1]  # 상하좌우 이동 시 y 값이 바뀌는 정도

# 위력 저장할 변수
w_power = 0
b_power = 0

# N명이 뭉치면 N**2 의 위력 (대각선은 NOPE)
# 그럼 인접한 애들끼리 찾자! BFS!!


def bfs(x, y, color):
    # 큐 구현
    queue = deque([(x, y)])  # 최초 시작 위치는 (0, 0)
    graph[x][y] = "V"       # 방문한 곳은 값을 V로 바꿈
    count = 1               # 뭉쳐있는 병사 수를 세기 위한 변수

    while queue:    # queue 가 빌 때까지 반복
        x, y = queue.popleft()     # 가장 먼저 삽입된 원소 꺼내기

        # 꺼낸 원소의 위치에서 상하좌우 탐색
        for i in range(4):
            search_x, search_y = x + dx[i], y + dy[i]
            # 범위 확인 필요 (그래프를 벗어나는 경우 제외) + 이미 방문한 곳인지 확인
            if 0 <= search_x < m and 0 <= search_y < n:
                if graph[search_x][search_y] == color:
                    queue.append((search_x, search_y))
                    graph[search_x][search_y] = "V"
                    count += 1

    return count


for i in range(m):
    for j in range(n):
        if graph[i][j] == "W":
            w_power += bfs(i, j, "W") ** 2
        elif graph[i][j] == "B":
            b_power += bfs(i, j, "B") ** 2

print(w_power, b_power)