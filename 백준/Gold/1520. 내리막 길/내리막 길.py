import sys
sys.setrecursionlimit(111111)
input = sys.stdin.readline

# i,j까지 갈수있는 경우의수
# dp[i][j] = sum(dp[i-1][j], dp[i+1][j], dp[i][j-1], dp[i+1][j+1])
# 가능한 경우에만
# O(N*M)
# ??? 걍 dfs아니야?
# 간선들을 먼저 파악해놓을까??
# DNC?


m, n = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(m)]
dp = [[-1]*n for _ in range(m)]
edges = {(i,j):[] for i in range(m) for j in range(n)}
answer = 0

dxs = [1,-1,0,0]
dys = [0,0,1,-1]

def is_possible(now_x,now_y,next_x,next_y):
    return 0<=next_x<m and 0<=next_y<n and graph[now_x][now_y]>graph[next_x][next_y]

    
def dfs(now_x, now_y):
    global answer
    if now_x==m-1 and now_y==n-1: return 1
    if dp[now_x][now_y]!=-1: return  dp[now_x][now_y]

    ways = 0

    for dx, dy in zip(dxs, dys):
        next_x, next_y = now_x+dx, now_y+dy
        if is_possible(now_x, now_y, next_x, next_y): ways+=dfs(next_x, next_y)

    dp[now_x][now_y] = ways

    return ways

print(dfs(0,0))
                