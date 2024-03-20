# 예시 n = 5, results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
def solution(n, results):
    answer = 0
    
    wins = [[] for _ in range(n+1)] # 1번 인덱스에는 1이 이긴(1에게 진) 선수가 담김
    loses = [[] for _ in range(n+1)] # 1번 인덱스에서는 1이 진(1에게 이긴) 선수가 담김
    
    for winner, loser in results:
        wins[winner].append(loser)
        loses[loser].append(winner)
    # wins = [[], [2], [5], [2], [3, 2], []]
    # loses = [[], [], [4, 3, 1], [4], [], [2]]
    
    for i in range(1, n+1):
        for w in wins[i]:
            # 1 > 2 > 5 (1이 2에게 이겼다면, 2에게 진 애들도 모두 1이 이긴다)
            for a in wins[w]:
                if a not in wins[i]:
                    wins[i].append(a)
            # 한 바퀴 돌면 [[], [2, 5], [5], [2], [3, 2], []]
        for l in loses[i]:
            for b in loses[l]:
                if b not in loses[i]:
                    loses[i].append(b)
            # 3이 4에게 졌다면, 4에게 이긴 애들도 모두 3을 이긴다 (3이 짐)
    print(wins)
    print(loses)
    # wins = [[], [2, 5], [5], [2, 5], [3, 2, 5], []]
    # loses = [[], [], [4, 3, 1], [4], [], [2, 4, 3, 1]]
    
    for i in range(1, n+1):
        if len(wins[i]) + len(loses[i]) == n-1:
            answer += 1
    
    return answer