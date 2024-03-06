n = int(input())
arr =  list(map(int, input().split()))
m = int(input())
test = list(map(int, input().split()))

arr = sorted(arr)

for t in test:
    start = 0
    end = n-1
    found = 0

    while start <= end:
        mid = (start + end) // 2
        
        if arr[mid] == t:
            found = 1
            break
        elif arr[mid] < t:
            start = mid + 1
        else:
            end = mid - 1
    print(found)
