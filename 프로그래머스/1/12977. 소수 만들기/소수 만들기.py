def solution(nums):
    answer = 0
    for i in range(len(nums)-2): # 첫번째 숫자
        for j in range(i+1, len(nums)-1): # 두번째 숫자
            for k in range(j+1, len(nums)): # 세번째 숫자
                sum = nums[i] + nums[j] + nums[k]
                for n in range(2, sum//2):
                    if sum % n == 0:
                        break
                else: # for문 다 돌고 나서 실행 (break 있으면 실행 안함)
                    answer += 1

    return answer