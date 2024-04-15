def make1(num):
    cnt = 0
    while num != 1:
        cnt += 1
        if num % 2:
            num = (num-1) // 2
        else:
            num = num // 2
    return cnt

def solution(num_list):
    return sum(make1(n) for n in num_list)