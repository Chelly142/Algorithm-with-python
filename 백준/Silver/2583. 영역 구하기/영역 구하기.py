#11:53 #12:31
from collections import deque

m,n,k = map(int,input().split())
g = [[0]*m for _ in range(n)]
for _ in range(k):
  a,b,c,d = map(int,input().split())
  for i in range(a,c):
    for j in range(b,d):
      g[i][j] = 1


d = [(1,0),(0,1),(-1,0),(0,-1)]
def bfs(s):
  q = deque([s])
  g[s[0]][s[1]] = 1
  cnt = 1
  while q:
    nn = q.popleft()
    for i in d:
      nx = nn[0]+i[0]
      ny = nn[1]+i[1]
      if n>nx>=0 and m>ny>=0 and g[nx][ny]==0:
        q.append((nx,ny))
        g[nx][ny] = 1
        cnt+=1
  return(cnt)

l =[]
t=0
for i in range(n):
  for j in range(m):
    if g[i][j] == 0:
      l.append(bfs((i,j)))
      t+=1
print(t)
l.sort()
print(*l)