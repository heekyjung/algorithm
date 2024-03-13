import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())  # n개의 줄에 m개의 정수로 미로가 주어짐 (n x m)

# 1은 이동할 수 있는 칸, 0은 이동할 수 없는 칸
graph = list(list(sys.stdin.readline().strip()) for _ in range(n))
# 예시 : [['1', '0', '1', '1', '1', '1'], ['1', '0', '1', '0', '1', '0'], ['1', '0', '1', '0', '1', '1'], ['1', '1', '1', '0', '1', '1']]

# 상하좌우 이동값 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, move=1):    # move = 칸 이동 횟수
    # 큐 생성
    queue = deque([(x, y, move)])   # 최초로 들어온 값 (x, y, move) 큐에 삽입
    graph[x][y] = move              # 방문한 곳은 몇 칸 이동했는지 저장

    while queue:    # 큐가 비게 될 때까지 반복
        x, y, move = queue.popleft()
        n_move = move + 1

        for i in range(4):  # 상하좌우 체크
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:  # 범위 확인
                if graph[nx][ny] == '1':
                    queue.append((nx, ny, n_move))
                    graph[nx][ny] = n_move
    
    return graph[n-1][m-1]

sys.stdout.write(f"{bfs(0, 0)}")