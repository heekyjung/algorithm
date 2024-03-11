# l = 암호를 구성하는 문자 개수, c = 후보 문자의 개수
l, c = map(int, input().split())
letters = list(input().split())  # 중복된 문자 없음

letters.sort()  # 문자열 오름차순 정렬
vowels = "aeiou"


def decrypt(code=""):
    if len(code) == l:  # 탈출 조건
        vowel_cnt = sum(1 for v in "aeiou" if v in code)
        consonant_cnt = len(code) - vowel_cnt
        if vowel_cnt >= 1 and consonant_cnt >= 2:
            print(code)
        return

    for i in range(len(letters)):
        if code == "" and i > (c-l):  # c-l 번째 인덱스 까지만 첫 문자가 될 수 있음
            break

        if not letters[i] in code: # 중복된 문자 없어야 함
            if code == "" or (code[-1] < letters[i]):
                code += letters[i]
                decrypt(code)
                code = code[:-1]


decrypt()