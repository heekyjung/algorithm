import sys
# sys.setrecursionlimit(10**7)
import heapq
# sys.stdin = open("sample_input.txt", "r")

# 정점의 개수 v, 간선의 개수 e
v, e = map(int, sys.stdin.readline().split())
# 시작 정점 k
k = int(sys.stdin.readline())


graph = {}
for i in range(1, v+1):
    graph[i] = {}

for _ in range(e):
    start, end, w = map(int, sys.stdin.readline().split())
    if end in graph[start]:
        graph[start][end] = min(graph[start][end], w)
    else:
        graph[start][end] = w

# 모든 정점까지의 소요시간을 무한대로 초기화
weights = {vertex: float('infinity') for vertex in graph}
heap = []


def dijkstra_heap(graph, start):
    # 시작 정점의 가중치는 0으로 초기화
    weights[start] = 0
    # (가중치, 현재 정점)
    heapq.heappush(heap, (0, start))

    while heap:
        w, n = heapq.heappop(heap)

        # 현재 정점과 연결된 다른 정점 확인
        for i, j in graph[n].items():
            nw = w + j
            if nw < weights[i]:
                weights[i] = nw
                heapq.heappush(heap, (nw, i))
    return weights


def dijkstra_no_heap(graph, start):
    # 각 정점을 방문했을 때, 이전에 방문한 정점을 기록
    previous_nodes = {vertex: None for vertex in graph}
    # 시작
    weights[start] = 0
    # 아직 방문하지 않은 모든 정점의 목록을 생성
    vertices_to_visit = list(graph.keys())

    # 방문하지 않은 정점이 남아있는 동안 계속 반복
    while vertices_to_visit:
        # 방문하지 않은 정점 중 가중치가 가장 낮은 도시 선택
        current_vertex = min(
            vertices_to_visit, key=lambda vertex: weights[vertex])

        # 선택된 정점의 가중치가 무한대라면, 나머지 정점은 모두 도달할 수 없는 것이므로 반복 종료
        if weights[current_vertex] == float('infinity'):
            break

        # 선택된 정점에 인접한 모든 정점에 대해 가중치 갱신
        for neighbor, weight in graph[current_vertex].items():
            # 선택된 정점을 거쳐 인접한 정점으로 이동하는 가중치 계산
            alternative_route = weights[current_vertex] + weight
            # 가중치가 현재 알려진 가중치 보다 저렴하면 갱신
            if alternative_route < weights[neighbor]:
                weights[neighbor] = alternative_route
                previous_nodes[neighbor] = current_vertex

        # 선택된 정점을 방문했으므로 목록 제거
        vertices_to_visit.remove(current_vertex)

    return weights


weights = dijkstra_heap(graph, k)
# weights = dijkstra_no_heap(graph, k)
for w in weights.values():
    if w == float('infinity'):
        print("INF")
    else:
        print(w)
