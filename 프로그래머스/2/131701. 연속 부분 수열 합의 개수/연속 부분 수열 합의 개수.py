def solution(elements):
    answer = 0
    l = []
    t = sum(elements)
    n = len(elements)

    for i in range(n): # i는 시작 원소 인덱스
        s=0
        for j in range(0,n-i-1):
            if i+j <n:
                s+=elements[i+j]
            else:
                s+=elements[i+j-n]
            l.append(s)
            l.append(t-s)
    answer = len(set(l))+1
    
    return answer