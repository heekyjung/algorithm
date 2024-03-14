import sys
from collections import deque
# sys.stdin = open("sample_input.txt", "r")

# n : 정점의 개수, m : 간선의 개수, v : 탐색을 시작하는 정점 번호
n, m, v = map(int, sys.stdin.readline().split())

pairs = list(sorted(list(map(int, sys.stdin.readline().split())))
             for _ in range(m))
# 예시 : [[4, 5], [2, 5], [1, 2], [3, 4], [1, 3]]

pairs_list = list([] for _ in range(n+1))
for p in pairs:
    if p[1] not in pairs_list[p[0]]:
        pairs_list[p[0]].append(p[1])
    if p[0] not in pairs_list[p[1]]:
        pairs_list[p[1]].append(p[0])
# 예시 : [[], [2, 3], [5, 1], [4, 1], [5, 3], [4, 2]]

for p in pairs_list:
    p.sort()
# 예시 : [[], [2, 3], [1, 5], [1, 4], [3, 5], [2, 4]]


dfs_visited = []
bfs_visited = []


def dfs(v):
    dfs_visited.append(str(v))
    for d in pairs_list[v]:
        if str(d) not in dfs_visited:
            dfs(d)
    return ' '.join(dfs_visited)


def bfs(v):
    queue = deque()
    queue.append(v)

    while queue:
        v = queue.popleft()
        bfs_visited.append(str(v))

        for p in pairs_list[v]:
            if str(p) not in bfs_visited and p not in queue:
                queue.append(p)

    return ' '.join(bfs_visited)


print(dfs(v))
print(bfs(v))