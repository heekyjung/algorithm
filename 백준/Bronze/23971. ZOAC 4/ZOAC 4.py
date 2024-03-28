import math
import sys
# sys.stdin = open("sample_input.txt", "r")

# 행의 개수 h, 열의 개수 w, 세로 n칸, 가로 m칸 이상 비워서 앉기
h, w, n, m = map(int, sys.stdin.readline().split())

print(math.ceil(h/(n+1)) * math.ceil(w/(m+1)))