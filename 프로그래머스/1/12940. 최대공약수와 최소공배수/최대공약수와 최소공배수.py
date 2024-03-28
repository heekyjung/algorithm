def gcd(n, m):
    while m:
        n, m = m, n%m
    return n

def solution(n, m):
    answer = [gcd(n, m), (n*m)//gcd(n, m)]
    return answer