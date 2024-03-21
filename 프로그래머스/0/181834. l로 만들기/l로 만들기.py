def solution(myString):
    str_list = []
    str_list += myString
    for i in range(len(str_list)):
        if str_list[i] < 'l':
            str_list[i] = 'l'
        
    return ''.join(str_list)