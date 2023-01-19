def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        flag = True
        p = 0
        for j in i:
            if j in skill:
                if p == skill.index(j):
                    p+=1
                else:
                    flag = False
                    break
        if flag:
            answer+=1
    return answer
