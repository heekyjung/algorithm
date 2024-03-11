n, m = map(int, input().split())  # n까지의 자연수 중에 중복 없이 m개를 고른 수열


def sequence(used=[]):
    if len(used) == m:  # 수열 길이가 m이 되면 리턴
        print(" ".join(map(str, used)))
        return

    for num in range(1, n+1):
        if (used == []) or (used[-1] < num):  # 수열에 값이 하나도 없거나 수열 마지막 값보다 크면 추가
            used.append(num)
            sequence(used)
            used.pop()


sequence()