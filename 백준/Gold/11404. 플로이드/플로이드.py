import sys
input = sys.stdin.readline

INF = int(10e9)

n = int(input())
m = int(input())
graph = [[10e9]*(n) for _ in range(n)]
for i in range(n):
    graph[i][i]=0
for _ in range(m):
    a,b,d = map(int,input().split())
    graph[a-1][b-1] = min(graph[a-1][b-1],d)

for mid in range(n):
    for start in range(n):
        for end in range(n):
            graph[start][end] = min(graph[start][end],graph[start][mid]+graph[mid][end])
for i in range(n):
    for j in range(n):
        if graph[i][j]==10e9:
            graph[i][j]=0
for row in graph:
    print(*row)

            


