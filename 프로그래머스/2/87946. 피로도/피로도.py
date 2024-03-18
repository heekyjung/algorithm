# k = 현재 피로도
# dungeons = [최소필요피로도, 소모피로도]의 2차원 배열
# 예: 80, [[80, 20], [50, 40], [30, 10]]

def dfs(k, cnt, dungeons, visited):
    global answer
    answer = max(answer, cnt)
    for i in range(len(dungeons)):
        req, con = dungeons[i]
        if visited[i] == False and req <= k:
            visited[i] = True
            dfs(k-con, cnt+1, dungeons, visited)
            visited[i] = False

def solution(k, dungeons):
    global answer
    visited = [False] * len(dungeons)
    answer = 0
    dfs(k, 0, dungeons, visited)
    
    return answer