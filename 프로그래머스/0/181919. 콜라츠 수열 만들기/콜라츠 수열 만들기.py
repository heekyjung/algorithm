def solution(n):
    answer = []
    answer.append(n)
    while n != 1:
        if n % 2:
            n = 3 * n + 1
        else:
            n = n // 2
        answer.append(n)
    return answer