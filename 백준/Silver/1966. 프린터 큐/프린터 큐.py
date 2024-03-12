import sys
from collections import deque

tc = int(sys.stdin.readline())  # 테스트케이스의 수

for _ in range(tc):
    # n = 문서의 개수, m = 인쇄 순서가 궁금한 문서의 위치 (0부터 시작)
    n, m = map(int, sys.stdin.readline().split())

    # doc_no : 문서가 최초에 큐에 들어간 순서, priorities : 중요도
    doc_no = deque([i for i in range(n)])
    priorities = deque(list(map(int, sys.stdin.readline().split())))

    order = 0   # 문서가 실제로 인쇄된 순서 기록

    while doc_no:
        if priorities[0] == max(priorities):
            order += 1
            printed = doc_no.popleft()
            priorities.popleft()
            if printed == m:
                break

        else:
            doc_no.append(doc_no.popleft())
            priorities.append(priorities.popleft())

    print(order)