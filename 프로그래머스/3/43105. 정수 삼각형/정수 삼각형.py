def solution(triangle):
    height = len(triangle)    
    answers = [[0 for _ in range(len(tri))] for tri in triangle]
    
    for i in range(height):
        for j in range(len(triangle[i])):
            before = 0
            if i - 1 >= 0:
                if j == 0:
                    before = answers[i-1][j]
                elif 0 < j < len(triangle[i])-1:
                    before = max(answers[i-1][j-1], answers[i-1][j])
                elif j == len(triangle[i]) - 1:
                    before = answers[i-1][j-1]
            sum = triangle[i][j] + before
            answers[i][j] = sum

    # [[7], [10, 15], [18, 16, 15], [20, 25, 20, 19], [24, 30, 27, 26, 24]]
    return max(answers[-1])
