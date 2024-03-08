T = int(input())
test_cases = list(input() for t in range(T))

for tc in test_cases:
    for i in range(1, len(tc)+1):
        pattern = tc[:i]
        post_pattern = tc[i:i*2]
        
        if pattern == post_pattern:
            pattern_length = len(pattern)
            break

    print(f"#{test_cases.index(tc) + 1} {pattern_length}")
