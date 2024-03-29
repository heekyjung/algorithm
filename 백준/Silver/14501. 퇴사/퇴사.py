import sys
# sys.stdin = open("sample_input.txt", "r")

# 상담이 가능한 기간 n (n+1일에 퇴사)
n = int(sys.stdin.readline())
schedules = [[] for _ in range(n+1)]
for i in range(1, n+1):
    schedules[i] = list(map(int, sys.stdin.readline().split()))
# [[], [3, 10], [5, 20], [1, 10], [1, 20], [2, 15], [4, 40], [2, 200]]
print(schedules)

dp = [0 for i in range(n+2)]

# 거꾸로 접근
for i in range(n, 0, -1):
    if i + schedules[i][0] - 1 > n:  # 퇴사일보다 오래 걸리면
        dp[i] = dp[i+1]
    else:  # 퇴사일보다 짧게 걸리면
        dp[i] = max(schedules[i][1] + dp[i + schedules[i][0]], dp[i+1])
    print(i)
    print(dp)

print(dp[1])
