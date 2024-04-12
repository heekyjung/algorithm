def solution(numbers):
    answer = 0
    for i in range(1, 10):
        answer += (i if i not in numbers else 0)
    return answer