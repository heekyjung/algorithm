def solution(x):
    s = sum([int(i) for i in list(str(x))])
    return False if x % s else True