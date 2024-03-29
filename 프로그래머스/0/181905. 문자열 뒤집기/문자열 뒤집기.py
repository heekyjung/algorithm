def solution(my_string, s, e):
    s_len = len(my_string)
    return my_string[:s] + my_string[-(s_len-e):-(s_len-s)-1:-1] + my_string[e+1:]