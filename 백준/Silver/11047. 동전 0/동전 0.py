n, k = map(int, input().split())
coins = []
for i in range(n):
    c = int(input())
    coins.append(c)

coins = list(reversed(coins))

answer = 0

for coin in coins:
    if (k // coin == 0) and (k % coin == 0):
        break
    answer += k // coin
    k = k % coin

print(answer)