from itertools import permutations

# 질문 횟수
tries = int(input())
num_list = list(permutations([1,2,3,4,5,6,7,8,9], 3))

for _ in range(tries):
    test, strike, ball = map(int, input().split())
    test = list(str(test))
    remove_cnt = 0

    for i in range(len(num_list)):
        s_cnt = b_cnt = 0
        i -= remove_cnt

        for j in range(3):
            test[j] = int(test[j])
            if test[j] in num_list[i]:
                if j == num_list[i].index(test[j]):
                    s_cnt += 1
                else:
                    b_cnt += 1

        if s_cnt != strike or b_cnt != ball:
            num_list.remove(num_list[i])
            remove_cnt += 1

print(len(num_list))