k, n = map(int, input().split())
length = [int(input()) for i in range(k)]

left = 1                # 최소 길이
right = max(length)     # 최대 길이

while left <= right:            # 최소 길이 ~ 최대 길이에서 이진 탐색
    mid = (left + right) // 2
    lan = 0     # 랜선 개수

    for i in length:
        lan += i // mid     # 현재 길이(mid)로 각 랜선에서 자른 개수 구하기
    
    if lan >= n:        # 필요한 랜선 개수 이상으로 만들면
        left = mid + 1  # mid+1 부터 right 까지 다시 탐색
    else:               # 필요한 랜선 개수 보다 적게 만들면
        right = mid -1  # left 부터 mid1 까지 다시 탐색

    # left 가 right 보다 커지면 자동으로 종료

print(right)