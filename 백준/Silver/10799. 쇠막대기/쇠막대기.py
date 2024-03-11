parentheses = input()

parentheses = parentheses.replace("()", "0") # 레이저는 0으로 변경

stack = []
total_sticks = 0
for p in parentheses:
    if p == "0": # 레이저라면 현재까지 스택에 쌓인 스틱 개수만큼 더함
        total_sticks += len(stack)
    elif p == "(": # 쇠막대가 시작하면 스택에 막대를 담는다.
        stack.append(1)
    elif p == ")": # 쇠막대가 끝나면 끝난 막대 하나를 스택 개수에 더하고, 스택에서 제거
        total_sticks += 1
        stack.pop()

print(total_sticks)