def count_div(x):
    count = 0
    for i in range(1, x+1):
        if x%i == 0:
            count += 1
    return count
            

def solution(left, right):
    answer = 0
    for n in range(left, right+1):
        if count_div(n) % 2:
            answer -= n
        else:
            answer += n
    return answer