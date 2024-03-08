def subsequence_sum(idx, sum):
    # 합이 k 값이 되는 경우의 수를 저장하기 위한 변수 (전역변수로 선언하여, 함수 종료 후에도 사라지지 않게 함)
    global count

    if idx >= n:  # 인덱스가 자연수 개수 이상이 되면 함수 종료
        return
    temp = sum + numbers[idx]
    if temp == k:
        count += 1

    subsequence_sum(idx + 1, temp)  # (현재 sum 값 + 이전 인덱스 값 + 새로운 인덱스 값)이 k 와 일치하는지 확인
    subsequence_sum(idx + 1, sum)   # (현재 sum 값 + 새로운 인덱스 값)이 k 와 일치하는지 확인


T = int(input())

for tc in range(T):
    n, k = map(int, input().split())  # n은 자연수 개수, k는 원하는 합
    numbers = list(map(int, input().split()))  # 자연수 리스트로 받기

    count = 0  # 각 케이스마다 0으로 초기화

    subsequence_sum(0, 0)  # 첫번째 0은 인덱스, 두번째 0은 합을 0으로 초기화하여 시작하는 것

    print(f"#{tc+1} {count}")
