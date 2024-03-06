n = int(input())
meetings = []
for i in range(n):
    m = list(map(int, input().split()))
    meetings.append(m)

meetings = sorted(meetings, key=lambda x: (x[1], x[0]))
end_time = 0
answer = 0

for m in meetings:
    if m[0] >= end_time:
        end_time = m[1]
        answer += 1

print(answer)
