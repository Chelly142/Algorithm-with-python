#3:05
def solution(n, s, a, b, fares):
    INF = 10e9
    answer = INF
    g= [[INF]*(n+1) for _ in range(n+1)]
    for i in range(1,n+1):
        g[i][i] = 0
    for fare in fares:
        x = fare[0]
        y = fare[1]
        v = fare[2]
        g[x][y] = v
        g[y][x] = v
    for m in range(1,n+1):
        for k in range(1,n+1):
            for e in range(1,n+1):
                t = min(g[k][m]+g[m][e],g[k][e])
                g[k][e] = t
                g[e][k] = t
    for node in range(1,n+1):
        answer=min(answer,g[s][node]+g[node][a]+g[node][b])

    return answer