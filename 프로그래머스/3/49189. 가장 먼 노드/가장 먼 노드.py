from collections import deque
def solution(n, edge):
    INF = 10e9 
    answer = 0
    g = [[] for _ in range(n+1)]
    for a,b in edge:
        g[a].append(b)
        g[b].append(a)
    d = [INF]*(n+1)
    d[1] = 0
    q = deque([1])
    
    while q:
        now = q.popleft()
        for i in g[now]:
            if d[i] == INF:
                d[i] = d[now]+1
                q.append(i)
    m = max(d[1:])
    for i in d:
        if i==m:
            answer+=1
    return answer