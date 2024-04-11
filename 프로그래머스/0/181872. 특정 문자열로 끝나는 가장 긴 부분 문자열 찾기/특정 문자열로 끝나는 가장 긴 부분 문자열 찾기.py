def solution(myString, pat):
    idx = myString.rfind(pat)
    return myString[:idx+len(pat)]