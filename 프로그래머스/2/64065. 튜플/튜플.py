#48분
def solution(s):
    answer = []
    token = s.split("},")
    for i in range(len(token)):
        t_s = ""
        for j in token[i]:
            if j not in "{}":
                t_s+=j
        token[i] = list(map(int,t_s.split(",")))
    token.sort(key=len)
    answer.append(token[0][0])
    for i in token:
        for j in i:
            if j not in answer:
                answer.append(j)
                break
    return answer