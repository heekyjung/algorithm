def solution(arr, queries):
    for q in queries:
        for i in range(len(arr)):
            if q[0] <= i <= q[1]:
                arr[i] += 1
    return arr