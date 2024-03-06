board = []
for i in range(9):
    board.append(list(map(int, input().split())))

answer = -1
for idx, row in enumerate(board):
    if max(row) > answer:
        answer = max(row)
        row_num = idx + 1
        col_num = row.index(max(row)) + 1

print(answer)
print(row_num, col_num)