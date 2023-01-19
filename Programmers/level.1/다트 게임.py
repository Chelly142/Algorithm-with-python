def solution(dartResult):
    answer = 0
    score = 0
    k=0
    a=[]
    for i,s in enumerate(dartResult):
        if s in [str(l) for l in range(10)]:
            if i!=0 and dartResult[i-1] == '1':
                score = 10
                continue
            score = int(s)
            k+=1
        elif s=='S':
            a.append(score)
        elif s=='D': 
            score = score**2
            a.append(score)
        elif s=='T':
            score = score**3
            a.append(score)
        elif s=='*':
            if k == 1:
                a[k-1] *= 2
            else:
                a[k-1] *= 2
                a[k-2] *= 2
        elif s=='#':
            a[k-1] *= -1
    print(a)            
    answer = sum(a)     
    return answer
