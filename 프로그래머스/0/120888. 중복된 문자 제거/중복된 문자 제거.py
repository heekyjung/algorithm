def solution(my_string):
    answer = ''
    for m in my_string:
        if m not in answer:
            answer += m
    return answer