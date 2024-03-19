from collections import deque
def solution(info, edges):
    answer= 0
    n = len(info)
    g = [[] for _ in range(n)]
    for x,y in edges:
        g[x].append(y)
    q=deque()
    q.append([0,g[0],1,0])
    while q:
        now,nxts,s,w = q.popleft()
        if answer < s:
            answer = s
        for i,nxt in enumerate(nxts):
            if info[nxt]==1:
                if s>w+1:
                    q.append([nxt,nxts[:i]+nxts[i+1:]+g[nxt],s,w+1])
            else:
                q.append([nxt,nxts[:i]+nxts[i+1:]+g[nxt],s+1,w])
                
        
    return answer