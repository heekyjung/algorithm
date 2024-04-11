def solution(absolutes, signs):
    num = []
    for a, s in zip(absolutes, signs):
        if s:
            num += [a]
        else:
            num += [-a]
    return sum(num)