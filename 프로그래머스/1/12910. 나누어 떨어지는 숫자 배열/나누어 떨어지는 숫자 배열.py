def solution(arr, divisor):
    answer = sorted([a for a in arr if a % divisor == 0]) or [-1]
    return answer