def solution(num):
    answer = 0
    i = 0
    while num != 1 and i < 500:
        i += 1
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
    return i if i < 500 else -1