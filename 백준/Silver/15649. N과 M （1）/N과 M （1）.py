n, m = map(int, input().split())

def sequence(used = []):
    if len(used) == m:
        print(" ".join(map(str, used)))
        return

    for num in range(1, n + 1):
        if not num in used:
            used.append(num)
            sequence(used)
            used.pop()

sequence()