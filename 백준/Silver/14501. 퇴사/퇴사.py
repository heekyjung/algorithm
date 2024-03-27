import sys
# sys.stdin = open("sample_input.txt", "r")

# 상담이 가능한 기간 n (n+1일에 퇴사)
n = int(sys.stdin.readline())
schedules = [[] for _ in range(n+1)]
for i in range(1, n+1):
    schedules[i] = list(map(int, sys.stdin.readline().split()))
# [[], [5, 50], [4, 40], [3, 30], [2, 20], [1, 10], [1, 10], [2, 20], [3, 30], [4, 40], [5, 50]]

dp = [0 for i in range(n+2)]

# 거꾸로 접근
for i in range(n, 0, -1):
    if i + schedules[i][0] - 1 > n:  # 퇴사일보다 오래 걸리면
        dp[i] = dp[i+1]
    else:  # 퇴사일보다 짧게 걸리면
        dp[i] = max(dp[i+1], schedules[i][1] + dp[i + schedules[i][0]])
    #print(dp)

print(dp[1])
