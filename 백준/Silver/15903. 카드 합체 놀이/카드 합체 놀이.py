import sys
import heapq

n, m  = map(int, sys.stdin.readline().split()) # 카드의 개수 n, 카드 합체 횟수 m
cards = list(map(int, sys.stdin.readline().split())) # 맨 처음 카드의 상태 (자연수)

heapq.heapify(cards)    # 최소 힙으로 구성하면 가장 위의 최소값부터 꺼내면서 더할 수 있다

for _ in range(m):  # 카드 합체 횟수만큼 반복
    num1 = heapq.heappop(cards)
    num2 = heapq.heappop(cards)

    result = num1 + num2
    heapq.heappush(cards, result)
    heapq.heappush(cards, result)

print(sum(cards))