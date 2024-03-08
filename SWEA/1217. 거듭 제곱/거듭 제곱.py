def power(base, exponent):
    if exponent < 1:
        return 1
    else:
        return base * power(base, exponent - 1)

for i in range(10):
    no = int(input())
    n, m = map(int, input().split())
    print(f"#{no} {power(n, m)}")
