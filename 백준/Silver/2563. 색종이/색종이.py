# 전체 도화지는 가로 100, 세로 100 -> 전체 도화지는 10,000칸 (1,1) ~ (100, 100)
# 색종이는 가로 10, 세로 10 -> 색종이 1개는 100칸

n = int(input())  # 색종이의 수 n (100 이하)
positions = [list(map(int, input().split())) for i in range(n)]  # 색종이 위치

# 도화지 칸 수만큼 리스트 만들기
paper = []
for i in range(1, 101):
    for j in range(1, 101):
        paper.append([i, j, 0]) # 2번 인덱스의 0은 색종이가 올라간 여부를 알기 위함

for pos in positions:
    # p에서 [3, 7] 이 들어오면, paper의 [4, 8] 칸부터 [13, 17] 까지 채워짐

    min_x = pos[0] + 1  # 색종이가 올라간 가장 낮은 x 좌표
    min_y = pos[1] + 1  # 색종이가 올라간 가장 낮은 y 좌표
    max_x = pos[0] + 10  # 색종이가 올라간 가장 높은 y 좌표
    max_y = pos[1] + 10  # 색종이가 올라간 가장 높은 y 좌표

    for pap in paper:
        if pap[0] >= min_x and pap[0] <= max_x and pap[1] >= min_y and pap[1] <= max_y:
            pap[2] = 1 # 색종이가 올라간 칸은 2번 인덱스의 값을 1로 값을 바꿈

count = sum(1 for pap in paper if pap[2] == 1) # 2번 인덱스가 1인 경우만 찾아서 세기
print(count)
