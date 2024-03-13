import sys
from collections import deque

# n : 라우터 내부의 버퍼 크기
n = int(sys.stdin.readline())

def router():
    queue = deque()
    input = int(sys.stdin.readline().strip())
    
    queue.append(input)

    # 들어오는 입력이 0 이상일 때만 반복. -1이 큐의 마지막 값으로 들어오면 반복문 종료
    while True:
        input = int(sys.stdin.readline().strip())

        if input == -1:
            break
        # 0이 들어오면 한 개 처리
        elif input == 0:
            queue.popleft()
        # 버퍼가 꽉 차 있으면 넣지 않고 다시 반복
        elif len(queue) == n:
            continue
        else:
            queue.append(input)

    if len(queue) == 0:
        output = "empty"
    else:
        output = ' '.join(str(x) for x in queue)

    return output

sys.stdout.write(f"{router()}")