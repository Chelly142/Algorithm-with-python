import sys
sys.setrecursionlimit(3000)
def dfs(x,y,m,n):
  g[x][y] = 0 
  if x+1<m and g[x+1][y] == 1:
    dfs(x+1,y,m,n)
  if x-1>=0  and g[x-1][y] == 1 :   
    dfs(x-1,y,m,n)
  if y+1<n and g[x][y+1] == 1  :
    dfs(x,y+1,m,n)
  if y-1>=0 and g[x][y-1] == 1  :
    dfs(x,y-1,m,n)

T = int(input())
for i in range(T):
  M,N,K = map(int,input().split())
  g = [[0]*N for _ in range(M)]
  answer = 0
  for j in range(K):
    a,b = map(int,input().split())
    g[a][b] = 1 
  for c in range(M):
    for d in range(N):
      if g[c][d]==1:
        dfs(c,d,M,N)
        answer+=1
  print(answer)