def hamburger(idx, score, cal):
    global max_score

    if cal > L: # 칼로리 초과
        return
    if score > max_score: # 현재 점수가 최대 점수보다 크면 저장
        max_score = score
    if idx == N: # 인덱스가 재료 수만큼 되면 종료
        return
    
    hamburger(idx + 1, score + ingredients[idx][0], cal + ingredients[idx][1]) # 현재 재료 선택
    hamburger(idx + 1, score, cal) # 현재 재료 미선택



T = int(input())  # 테스트 케이스 수

for tc in range(T):
    N, L = map(int, input().split())  # N은 재료의 수, L은 제한 칼로리
    ingredients = [list(map(int, input().split())) for n in range(N)] # [점수, 칼로리]

    max_score = 0
    hamburger(0, 0, 0)
    

    print(f"#{tc+1} {max_score}")
