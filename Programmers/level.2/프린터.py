def solution(priorities, location):
    answer = 1
    np = []
    for i,v in enumerate(priorities):
        np.append([i,v])
    while(np):
        m = max(np,key = lambda x:x[1])
        if m[0] == location:
            break
        i = np.index(m)
        if i==0:
            del np[0]
            answer += 1
            
        else:
            np = np[i:] + np[:i]
            del np[0]
            answer += 1
    return answer
