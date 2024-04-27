def solution(k, score):
    answer = []
    l = []
    for i in score:
        l.append(i)
        l.sort(reverse=True)
        if len(l)<k:
            answer.append(l[-1])
        else:
            answer.append(l[k-1])
    return answer