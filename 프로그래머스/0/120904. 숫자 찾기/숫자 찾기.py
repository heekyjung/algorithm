def solution(num, k):
    num_list = list(str(num))
    if str(k) in num_list:
        answer = num_list.index(str(k))+1
    else:
        answer = -1
    return answer