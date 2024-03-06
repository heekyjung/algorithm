n = int(input())

for i in range(n):
    result = i + sum(map(int, list(str(i))))
    if result == n:
        answer = i
        break
    answer = 0

print(answer)