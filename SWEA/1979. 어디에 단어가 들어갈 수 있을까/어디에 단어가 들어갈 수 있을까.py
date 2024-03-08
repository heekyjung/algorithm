T = int(input())

for tc in range(T):
    n, k = map(int, input().split())  # n은 단어 퍼즐의 가로세로 길이, k는 단어의 길이
    puzzle = [list(map(int, input().split())) for n in range(n)]  # 단어 퍼즐
    answer = 0  # 정답 저장

    for i in range(n):
        count = 0
        # 가로줄 확인
        for j in range(n):
            if puzzle[i][j] == 1:  # 퍼즐이 1일 때
                count += 1
            if puzzle[i][j] == 0 or j == n-1:  # j==n-1 없으면, 마지막 칸에서 끝나는 경우를 셀 수 없음
                if count == k:  # 지금까지 쌓은 카운트가 단어 길이와 같다면 answer 올리기
                    answer += 1
                count = 0  # 다시 초기화

        # 세로줄 확인
        for j in range(n):
            if puzzle[j][i] == 1:
                count += 1
            if puzzle[j][i] == 0 or j == n-1:
                if count == k:
                    answer += 1
                count = 0

    print(f"#{tc+1} {answer}")
