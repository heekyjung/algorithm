import sys
# sys.stdin = open("sample_input.txt", "r")

n = int(sys.stdin.readline())
wires = []
for _ in range(n):
    wires.append(list(map(int, sys.stdin.readline().split())))
# [[1, 8], [3, 9], [2, 2], [4, 1], [6, 4], [10, 10], [9, 7], [7, 6]]
wires.sort()
# [[1, 8], [2, 2], [3, 9], [4, 1], [6, 4], [7, 6], [9, 7], [10, 10]]

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if wires[i][1] > wires[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)
        #print("i", i, "j", j, dp)

print(n-max(dp))