def solution(myString):
    str_list = myString.split("x")
    return list(map(len, str_list))