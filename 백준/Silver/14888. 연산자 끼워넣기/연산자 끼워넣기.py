n = int(input())  # 수의 개수 n
numbers = list(map(int, input().split()))  # 계산할 숫자 리스트
operators = list(map(int, input().split()))  # +, -, *, // 의 개수

result = [-1000000000, 1000000000]  # 계산 결과 저장


def cal(answer=numbers[0], idx=1):

    if idx == n:  # idx 가 숫자 개수만큼 되면 최종 계산 결과 저장하고, 함수 종료
        result[0] = max(answer, result[0])
        result[1] = min(answer, result[1])
        return

    for i in range(4):
        if operators[i] > 0:
            operators[i] -= 1
            if i == 0:  # 덧셈
                cal(answer + numbers[idx], idx + 1)
            elif i == 1:  # 뺄셈
                cal(answer - numbers[idx], idx + 1)
            elif i == 2:  # 곱셈
                cal(answer * numbers[idx], idx + 1)
            elif i == 3:  # 나눗셈 (answer가 음수일 때 변환해서 정수로 계산이 안되어 변환 필요)
                cal(int(answer / numbers[idx]), idx + 1)
            operators[i] += 1


cal()
print(result[0])
print(result[1])
