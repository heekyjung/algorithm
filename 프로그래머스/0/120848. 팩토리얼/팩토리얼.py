def solution(n):
    i, fac = 1, 1
    while fac <= n:
        fac = 1
        j = i 
        while j > 1:
            fac *= j
            j -= 1
        i += 1
    return i-2