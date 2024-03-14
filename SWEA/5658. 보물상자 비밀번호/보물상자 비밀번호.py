from collections import deque
# import sys
# sys.stdin = open("sample_input.txt", "r")


# 테스트 케이스의 수 T
T = int(input())

for t in range(1, T+1):
    # n : 숫자의 개수 , k : 크기 순서
    n, k = map(int, input().split())
    # 16진수
    numbers = deque(list(input()))

    # 비밀번호 길이 (n은 4의 배수, 8 이상, 28 이하)
    length = n // 4
    # 회전의 경우의 수는 length 만큼!

    # 비번 후보 담기
    combinations = []

    # 회전 수만큼 반복
    for l in range(length):
        # 이번 회전에 나온 비번 개수만큼 가져오기
        for i in range(4):
            password = ''
            for j in range(length):
                password += numbers[length * i + j]
            if password not in combinations:
                combinations.append(password)
        num = numbers.popleft()
        numbers.append(num)

    # 16진수로 쓰기 int("문자열", 16)
    result = list(map(lambda x: int(x, 16), combinations))
    result.sort(reverse=True)
    print(f"#{t} {result[k-1]}")
