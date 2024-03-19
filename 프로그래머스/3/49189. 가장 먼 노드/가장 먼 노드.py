# 노드의 개수 n, 간선에 대한 정보가 담긴 2차원 배열 edge
# 예시 : [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

from collections import deque

def solution(n, edge):
    # 노드 1부터 각 노드까지의 거리 리스트
    distances = [0] * (n+1)
    # 각 노드에서 연결된 노드 번호 리스트
    graph = [[] for _ in range(n+1)]
    # 연결된 노드 정보 저장
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    
    queue = deque()
    queue.append(1)
    distances[1] = 1
    
    while queue:
        now = queue.popleft()
        
        for linked in graph[now]:
            if distances[linked] == 0:
                distances[linked] = distances[now] + 1
                queue.append(linked)
    
    answer = distances.count(max(distances))
    
    return answer