import sys

n = int(sys.stdin.readline())  # 도시의 개수 n
m = int(sys.stdin.readline())  # 버스의 개수 m

graph = {}
for i in range(1, n+1):
    graph[i] = {}

for _ in range(m):
    start, end, cost = map(int, sys.stdin.readline().split())
    if end in graph[start]:
        graph[start][end] = min(graph[start][end], cost)
    else:
        graph[start][end] = cost

city1, city2 = map(int, sys.stdin.readline().split())


def dijkstra(graph, start):
    # 모든 도시까지의 요금을 무한대로 초기화
    costs = {vertex: float('infinity') for vertex in graph}
    # 각 도시를 방문했을 때, 이전에 방문한 도시를 기록
    previous_nodes = {vertex: None for vertex in graph}
    # 시작 도시 요금 0으로 초기화
    costs[start] = 0
    # 아직 방문하지 않은 모든 도시의 목록을 생성
    vertices_to_visit = list(graph.keys())

    # 방문하지 않은 도시가 남아있는 동안 계속 반복
    while vertices_to_visit:
        # 방문하지 않은 도시 중 요금이 가장 낮은 도시 선택
        current_vertex = min(
            vertices_to_visit, key=lambda vertex: costs[vertex])

        # 선택된 도시의 요금이 무한대라면, 나머지 도시는 모두 도달할 수 없는 것이므로 반복 종료
        if costs[current_vertex] == float('infinity'):
            break

        # 선택된 도시에 인접한 모든 도시에 대해 요금 갱신
        for neighbor, weight in graph[current_vertex].items():
            # 선택된 도시를 거쳐 인접한 도시로 이동하는 요금 계산
            alternative_route = costs[current_vertex] + weight
            # 계산된 요금이 현재 알려진 요금보다 저렴하면 갱신
            if alternative_route < costs[neighbor]:
                costs[neighbor] = alternative_route
                previous_nodes[neighbor] = current_vertex

        # 선택된 도시를 방문했으므로 목록 제거
        vertices_to_visit.remove(current_vertex)

    # 모든 도시까지의 최소 요금 정보 반환
    return costs


print(dijkstra(graph, city1)[city2])