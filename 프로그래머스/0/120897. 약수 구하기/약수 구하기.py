def solution(n):
    answer = []
    for i in range(1, n+1):
        if i in answer:
            break
        if n % i == 0:
            answer.append(i)
            if i != n//i:
                answer.append(n//i)
    return sorted(answer)