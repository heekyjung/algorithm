import sys
sys.setrecursionlimit(10**7)
# sys.stdin = open("sample_input.txt", "r")

# 정점 개수 n, 간선 개수 m
n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)
# graph : [[], [2, 5], [1, 5], [4], [3, 6], [2, 1], [4]]

count = 0


def dfs(node):
    if visited[node]:  # 탈출 조건
        return

    visited[node] = True
    for n in graph[node]:
        if visited[n] == False:
            dfs(n)


for i in range(1, n+1):
    if visited[i] == False:
        dfs(i)
        count += 1

print(count)