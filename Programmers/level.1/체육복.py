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

def solution(n, lost, reserve):
    l = [1]*(n+2)
    for i in lost:
        l[i]-=1
    for i in reserve:
        l[i]+=1
    for i in range(1,n+1):
        if l[i]==2 and l[i-1]==0:
            l[i-1]=1
            l[i]=1
        elif l[i]==2 and l[i+1]==0:
            l[i+1]=1
            l[i]=1
    return n - l.count(0)
