def solution(n):
    answer = []
    def hanoi(d,f,t,v):
        if d==1:
            answer.append([f,t])
        else:
            hanoi(d-1,f,v,t)
            answer.append([f,t])
            hanoi(d-1,v,t,f)
    hanoi(n,1,3,2)
    return answer