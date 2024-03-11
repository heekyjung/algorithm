n = int(input())  # n : 컴퓨터의 수 (100 이하의 양의 정수)
# 컴퓨터는 1번부터 번호 매겨짐

pairs = int(input())  # 연결된 컴퓨터 쌍의 수

# [[], [1번 컴퓨터와 연결된 컴퓨터], ..., [n번 컴퓨터와 연결된 컴퓨터]]
connected = [[] for _ in range(n+1)]

for _ in range(pairs):
    com1, com2 = map(int, input().split())
    connected[com1].append(com2)    # com1과 연결된 com2 번호를 com1 인덱스의 리스트에 삽입
    connected[com2].append(com1)    # com2과 연결된 com1 번호를 com2 인덱스의 리스트에 삽입

infected = set()    # 감염된 컴퓨터 표시

def dfs(com):
    infected.add(com)
    for c in connected[com]:
        if c not in infected:
            dfs(c)

dfs(1)                  # 1번 컴퓨터부터 감염 시작
print(len(infected)-1)  # 최초 감염 컴퓨터 제외하고 출력