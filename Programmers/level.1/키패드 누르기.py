def solution(numbers, hand):
    answer = ''
    matrix = [[4,2],[1,1],[1,2],[1,3],[2,1],[2,2],[2,3],[3,1],[3,2],[3,3],[4,1],[4,3]]
    l = 10
    r = 11
    for i in numbers:
        
        if i in [1,4,7]:
            answer = answer + "L"
            l = i
        elif i in [3,6,9]:
            answer = answer + "R"
            r = i
        elif i in [2,5,8,0]:
            l_d = abs(matrix[i][0] - matrix[l][0]) + abs(matrix[i][1] - matrix[l][1])
            r_d = abs(matrix[i][0] - matrix[r][0]) + abs(matrix[i][1] - matrix[r][1])
            if l_d > r_d:
                answer = answer + "R"
                r = i
            elif r_d > l_d:
                answer = answer + "L"
                l = i
            elif hand == "right":
                answer = answer + "R"
                r = i
            else:
                answer = answer + "L"
                l = i
                
    return answer
