import sys
from collections import deque

# 트럭의 순서 못 바꾸고, 
# n : 다리를 건너는 트럭의 수, w : 다리의 길이, l : 다리의 최대하중
n, w, l = map(int, sys.stdin.readline().split())

# i번째 트럭의 무게 (1~10 사이 정수)
trucks = list(map(int, sys.stdin.readline().split()))
t_queue = deque(trucks)

def bfs():
    # 다리 위에 올라간 큐
    b_queue = deque([0] * (w-1))        # 첫번째 트럭이 다 건너기 위해 가야할 시간만큼 큐에 0 으로 추가
    b_queue.append(t_queue.popleft())   # 대기 중인 트럭 목록 중 첫번째 빼서 다리 위로 올리기
    time = 1

    while b_queue:
        b_queue.popleft()
        time += 1

        # 대기 중인 트럭이 있을 때
        if t_queue:
            # 다리 위 트럭 무게 합 + 추가될 트럭 무게 합 <= 최대 하중 이어야 트럭 추가 가능
            if sum(b_queue) + t_queue[0] <= l:
                b_queue.append(t_queue.popleft())

            # 트럭이 올라가지 못하면 공기(0가 올라간다
            else:
                b_queue.append(0)

    return time

print(bfs())