n = int(input())
g = [list(input()) for _ in range(n)]
k = [0]*(n*n)

def dfs(x,y,a):
  g[x][y] = 'v'
  k[a]+=1
  if x+1<n and g[x+1][y] == '1':
    dfs(x+1,y,a)
  if x-1>=0 and g[x-1][y] == '1':
    dfs(x-1,y,a)
  if y+1<n and g[x][y+1] == '1':
    dfs(x,y+1,a)
  if y-1>=0 and g[x][y-1] == '1':
    dfs(x,y-1,a)
  

c=0
for i in range(n):
  for j in range(n):
    if g[i][j] == '1':
      dfs(i,j,c)
      c+=1
print(c)
for i in sorted(k):
  if i !=0:
    print(i)