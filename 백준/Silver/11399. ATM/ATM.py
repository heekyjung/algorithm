n = int(input())
p = list(map(int, input().split()))
p = sorted(p)

time = 0
total_time = 0

for i in range(n):
    time += p[i]
    total_time += time

print(total_time)