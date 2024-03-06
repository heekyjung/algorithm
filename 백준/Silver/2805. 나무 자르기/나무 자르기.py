n, m = map(int, input().split())         # 나무의 수 n, 필요한 나무 길이 m
trees = list(map(int, input().split()))  # 나무의 높이

left = 1
right = max(trees)

while left <= right:
    mid = (left + right) // 2
    cut = 0

    for tree in trees:
        if tree > mid:
            cut += tree - mid

    if cut >= m:
        left = mid + 1
    else:
        right = mid - 1

print(right)
