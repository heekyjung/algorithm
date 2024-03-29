def solution(arr, queries):
    answer = []
    for q in queries:
        nums = [arr[i] for i in range(len(arr)) if q[0] <= i <= q[1] and arr[i] > q[2]]
        answer.append(min(nums) if nums else -1)
    return answer