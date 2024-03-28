hour, minute = map(int, input().split())
if minute < 45:
    hour -= 1
    minute += 15
    if hour < 0:
        hour = 23
else:
    minute -= 45
print(f"{hour} {minute}")