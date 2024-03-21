def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    
    def dfs(com):
        if visited[com]:
            return
        visited[com] = True
        for w in range(n):
            if w != com and computers[com][w] == 1:
                if visited[w] == False:
                    dfs(w)
    
    for i in range(n):
        if visited[i] == False:
            dfs(i)
            answer += 1

    return answer