import sys
import heapq

n = int(sys.stdin.readline())

numbers = []           # 배열 선언

for _ in range(n):
    numbers.append(int(sys.stdin.readline()))

num_heap = []           # 힙 만들 배열 저장
heapq.heapify(num_heap) # 최소 힙

output = numbers.count(0)   # 필요한 출력 횟수 저장
printed = 0                 # 출력 횟수 저장할 변수

for num in numbers:
    if num > 0:                         # 자연수라면
        heapq.heappush(num_heap, -num)  # 배열에 값을 넣는다. (최대 힙으로 해야하므로, 반대로 '-'를 붙여줌)
    else:   # num = 0 일 때
        if num_heap:                        # 힙에 값이 있다면
            print(-heapq.heappop(num_heap)) # 가장 작은 값 제거면서 그 값을 출력 (원래 값 출력 위해 - 붙임)
        else:           # 힙에 원소가 없다면
            print(0)    # 0 출력