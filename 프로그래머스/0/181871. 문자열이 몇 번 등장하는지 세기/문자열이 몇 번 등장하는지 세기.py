def solution(myString, pat):
    answer = 0
    for i in range(len(myString)-len(pat)+1):
        if pat == myString[i:i+len(pat)]:
            answer += 1
    return answer