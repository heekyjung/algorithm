def solution(n):
    x = n**0.5
    return (x+1)**2 if n % x == 0 else -1