T = int(input())
text_list = [input() for i in range(T)]

for text in text_list:
    is_palindrome = -1
    import math
    for i in range(math.ceil(len(text) / 2)):

        if text[i] != text[len(text) - 1 - i]:
            is_palindrome = 0
            break
        else:
            is_palindrome = 1

    print(f"#{text_list.index(text) + 1} {is_palindrome}")
