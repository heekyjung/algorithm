def solution(numLog):
    answer = ''
    for i in range(-1, -len(numLog), -1):
        a, b = numLog[i-1], numLog[i]
        if b - a == 1:
            answer = 'w' + answer
        elif a - b == 1:
            answer = 's' + answer
        elif b - a == 10:
            answer = 'd' + answer
        elif a - b == 10:
            answer = 'a' + answer
    return answer