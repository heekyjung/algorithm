# 테스트 케이스의 수 t
t = int(input())


def preorder(n):
    global count

    if n:   # n이 0이 아닐 때만
        count += 1
        preorder(left[n])
        preorder(right[n])


for case in range(1, t + 1):
    # e : 부모-자식 노드 쌍의 개수, n : 기준이 되는 노드
    e, n = map(int, input().split())

    input_list = list(map(int, input().split()))

    left = [0] * (e+2)
    right = [0] * (e+2)
    count = 0

    for i in range(0, len(input_list), 2):
        parent, child = input_list[i], input_list[i+1]

        if left[parent] == 0:
            left[parent] = child
        else:
            right[parent] = child

    preorder(n)

    print(f"#{case} {count}")
