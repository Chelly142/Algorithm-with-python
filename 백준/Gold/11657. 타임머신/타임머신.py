import sys
input = sys.stdin.readline

INF = int(10e9)

n,m = map(int, input().split())

edges = [tuple(map(int,input().split())) for _ in range(m)]


def bellman(start):
    distances = [INF]*(n+1)
    distances[start] = 0
    for i in range(n):
        for j in range(m):
            cur_node, nxt_node, cost = edges[j]
            if distances[cur_node]!=INF and distances[cur_node] + cost < distances[nxt_node]:
                distances[nxt_node] = distances[cur_node] + cost
                if i==n-1:
                    return False
    return distances

if bellman_1:=bellman(1):
    for i in range(2,n+1):
        if bellman_1[i]==INF: print(-1)
        else: print(bellman_1[i])
else: print(-1)
