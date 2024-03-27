import sys
# sys.stdin = open("sample_input.txt", "r")

# 일곱 난쟁이의 키 입력 받기
heights = []
for _ in range(9):
    heights.append(int(sys.stdin.readline()))
# 키 정렬
heights.sort()

found = False
for i in range(9):
    for j in range(i+1, 9):
        if sum(heights) - heights[i] - heights[j] == 100:
            del1, del2 = i, j  # 삭제할 난쟁이 인덱스
            found = True
            break

    if found:
        # 두 난쟁이를 리스트에서 제거
        heights.pop(del2)
        heights.pop(del1)
        break

for height in heights:
    print(height)
