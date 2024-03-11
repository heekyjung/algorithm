n = int(input())

# 크기가 n인 리스트를 만들어서, 각 줄당 퀸이 위치하는 인덱스를 값으로 두면 2차원 배열을 안 만들고 해결 가능!
queens = [-1] * n    # n = 4이면, [-1, -1, -1, -1] (인덱스가 아닌 -1을 초기값 지정)
result = 0


def is_valid(row, col):
    for i in range(row):    # 현재 체크하는 행의 이전 행까지만 확인!
        # 같은 열에 위치한 퀸이 있을 때 or 양쪽 대각선 방향에 퀸이 존재할 때
        if (queens[i] == col) or (abs(queens[i] - col) == abs(i - row)):
            return False
    return True


def n_queens(row):
    global result

    if row == n:    # 모든 행 탐색 완료
        result += 1
        return

    for col in range(n):
        queens[row] = col       # 지금 행, 열 위치에 퀸을 두기
        if is_valid(row, col):       # 퀸의 위치가 괜찮은지 체크
            n_queens(row + 1)   # 괜찮으면 row 하나 높여서 다시 진행


n_queens(0)
print(result)