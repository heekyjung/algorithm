import heapq

# import sys
# sys.stdin = open("input.txt", "r")

# T : 테스트 케이스의 수
T = int(input())

for t in range(1, T+1):
    # N : 수행해야 하는 연산의 수
    N = int(input())

    max_heap = []
    heapq.heapify(max_heap)

    delete = []

    for _ in range(N):
        op_num = list(map(int, input().split()))
        if op_num[0] == 1:
            heapq.heappush(max_heap, -op_num[1])
        elif op_num[0] == 2:
            if max_heap:    # 힙에 값이 있으면
                delete.append(str(-heapq.heappop(max_heap)))
            else:           # 힙이 비어있으면
                delete.append(str(-1))
    
    print(f"#{t} {' '.join(delete)}")
