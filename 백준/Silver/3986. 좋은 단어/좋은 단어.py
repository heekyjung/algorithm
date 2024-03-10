n = int(input())

def good_word(text):
    stack = []
    
    for t in text:
        if (len(stack) == 0) or (stack[-1] != t):
            stack.append(t)
        else: # t와 stack의 마지막 값이 같다면 짝이 맞는 걸로 판단하면 스택에서 제거
            stack.pop()
    
    return (0 if stack else 1)

count = 0

for i in range(n):
    word = input()
    count += good_word(word)

print(count)