T = int(input())
test_cases = list(input() for t in range(T))

mirrored_text = {'b': 'd', 'd': 'b', 'p': 'q', 'q': 'p'} # 각 문자별로 거울문자 저장

for tc in test_cases:
    tc_list = list(tc)
    for i in range(len(tc_list)):
        tc_list[i] = mirrored_text[tc_list[i]]
    mirrored_tc = ''.join(tc_list)
    
    print(f"#{test_cases.index(tc) + 1} {mirrored_tc[::-1]}")
