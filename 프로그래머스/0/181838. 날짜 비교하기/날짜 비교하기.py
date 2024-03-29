from datetime import datetime
def solution(date1, date2):
    d1 = datetime(date1[0], date1[1], date1[2])
    d2 = datetime(date2[0], date2[1], date2[2])
    return int((d2-d1).days>0)