for tc in range(1, 11):
    length = int(input())  # 찾아야 하는 회문의 길이 length
    rows = list(input() for i in range(8))  # 글자판 받기

    count = 0  # 찾은 회문 저장할 변수

    # 가로줄 탐색
    for row in rows:  # 줄 8개 돌기
        for r in range(9-length):
            text = row[r:r+length]
            text_reversed = text[::-1]
            count += (1 if text == text_reversed else 0)

    # 세로줄 탐색
    for col in range(8):
        col_text = ''.join([rows[r_idx][col] for r_idx in range(8)])  # 세로줄 기준으로 텍스트 만들기
        for c in range(9-length):
            text = col_text[c:c+length]
            text_reversed = text[::-1]
            count += (1 if text == text_reversed else 0)

    print(f"#{tc} {count}")
