def solution(n, lost, reserve):
    answer = 0
    for i in lost[:]:
        if i in reserve:
            lost.remove(i)
            reserve.remove(i)
            answer = answer + 1
    for i in lost[:]:
        if i-1 in reserve:
            lost.remove(i)
            reserve.remove(i-1)
            continue
        elif i+1 in reserve:
            lost.remove(i)
            reserve.remove(i+1)
            continue
    answer = n - len(lost)
    return answer
