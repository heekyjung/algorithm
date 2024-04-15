def solution(array, n):
    answer = float("inf")
    diff = float("inf")
    for arr in array:
        temp = abs(n - arr)
        if temp <= diff:
            if temp == diff:
                answer = min(arr, answer)
            else:
                answer = arr
            diff = temp
    return answer