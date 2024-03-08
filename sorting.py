# 버블정렬
print("버 블 정 렬")

temp_list = [3, 6, 15, 1, 7, 2, 5, 20, 7, 12, 4]

bubble_step = 0


def bubble_sort(num_list, length):
    global bubble_step
    swap = 0
    for i in range(length - 1):
        if num_list[i] > num_list[i+1]:
            num_list[i], num_list[i+1] = num_list[i+1], num_list[i]
            swap += 1
        else:
            continue

    if swap == 0:  # swap이 한번도 발생하지 않으면 함수 종료
        return num_list

    length -= 1  # 재귀함수 호출 시, 이미 정렬된 마지막 데이터까지 반복하지 않기 위함
    bubble_step += 1
    print(f"버블{bubble_step}: {num_list}")
    return bubble_sort(num_list, length)


print(bubble_sort(temp_list, len(temp_list)))
print("-"*40)

# 선택정렬
print("선 택 정 렬")

# 선택 정렬은 중복된 값이 존재하면 swap 이 일어나 정렬이 제대로 안됨
temp_list = [60, 20, 70, 10, 80, 30, 50, 40]


def selection_sort(num_list):
    for i in range(len(num_list)-1):
        min_num = min(num_list[i:])
        min_idx = num_list.index(min_num)
        if num_list[i] > num_list[min_idx]:
            num_list[i], num_list[min_idx] = num_list[min_idx], num_list[i]

        print(f"선택{i+1}: {num_list}")
    return num_list


print(selection_sort(temp_list))
print("-"*40)


# 삽입정렬
print("삽 입 정 렬")

temp_list = [60, 20, 70, 10, 80, 30, 50, 40]


def insertion_sort(num_list):
    for i in range(1, len(num_list)):
        data = num_list[i]

        for j in reversed(range(0, i)):  # 정렬된 데이터 역순으로 순회
            if num_list[j] <= data:  # data가 정렬된 데이터 값보다 크면 오른쪽에 배치
                num_list.pop(i)
                num_list.insert(j+1, data)
                break
            elif j == 0:  # 마지막 인덱스가 되면
                num_list.pop(i)
                num_list.insert(0, data)
                break
            else:  # 그 외에 data가 정렬된 데이터 값보다 작으면 반복문 계속 돌기
                continue
        print(f"삽입{i}: {num_list}")

    return num_list


print(insertion_sort(temp_list))
print("-"*40)

# 병합정렬
print("병 합 정 렬")


def merge(left_list, right_list):
    merged_list = []

    while left_list or right_list:  # 두 리스트가 모두 비어있으면, while문 종료
        if not left_list:  # 리스트 한쪽이 빈 경우, 나머지 리스트를 전부 넣는 코드 (없으면 out of value)
            merged_list += right_list
            right_list = False
        elif not right_list:
            merged_list += left_list
            left_list = False
        else:
            if left_list[0] >= right_list[0]:  # right 값이 더 작으면
                merged_list.append(right_list[0])  # right 값을 넣고 뺀다
                right_list.pop(0)
            else:
                merged_list.append(left_list[0])
                left_list.pop(0)

    print(f"병합: {merged_list}")
    return merged_list


def merge_sort(num_list):
    length = len(num_list)
    mid = (length // 2 + 1 if length %
           2 else length // 2)  # 원소 개수의 홀짝 여부에 따라 중앙값 설정

    left, right = num_list[:mid], num_list[mid:]  # 두 리스트에 나눠서 담기
    print(left, right)

    if mid == 1:  # 원소 개수가 한개가 되면 병합 (중앙값이 1이면 양쪽 원소가 1개씩)
        return merge(left, right)

    left = merge_sort(left)   # 계속 쪼개기
    right = merge_sort(right)

    return merge(left, right)


temp_list = [54, 34, 41, 89, 67, 16, 52, 23, 3]
print(merge_sort(temp_list))

