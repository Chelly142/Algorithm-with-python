def solution(d, budget):
    answer = 0
    d.sort()
    for i,v in enumerate(d):
        if budget<v:
            return i
        else:
            budget-=v
    return len(d)
