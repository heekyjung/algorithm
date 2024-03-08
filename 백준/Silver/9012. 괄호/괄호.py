T = int(input())

def isVps(text):
    vpsStack = []

    for t in text:
        if t == "(":
            vpsStack.append(t)
        else:  # t가 ) 일 때
            if not vpsStack:  # 스택에 아무것도 안 들어있고, 시작은 ) 로 하면 바로 NO
                return "NO"
            else:
                vpsStack.pop()
    return "NO" if vpsStack else "YES"


for tc in range(T):
    print(isVps(input()))