import sys
# sys.setrecursionlimit(10**7)
# sys.stdin = open("sample_input.txt", "r")

# 전체 사람의 수 n
n = int(sys.stdin.readline())
# 촌수 계산을 하는 두 사람
p1, p2 = map(int, sys.stdin.readline().split())
# 부모 자식 간의 관계의 개수 m
m = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]  # n번 인덱스의 부모가 담김
visited = [False for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[y].append(x)
    graph[x].append(y)
# graph : [[], [2, 3], [1, 7, 8, 9], [1], [5, 6], [4], [4], [2], [2], [2]]


def dfs(node, count=0):
    global answer
    # print(node, count)
    visited[node] = True
    if node == p2:
        answer = count
        return

    for g in graph[node]:
        if not visited[g]:
            # print(g)
            dfs(g, count+1)
    return answer


answer = 0
dfs(p1)
print(answer if answer > 0 else -1)