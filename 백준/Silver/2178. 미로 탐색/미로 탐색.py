#10:21
from collections import deque

n,m = map(int,input().split())
g = [list(input()) for _ in range(n)]
d = [(1,0),(0,1),(-1,0),(0,-1)]
def bfs():
  q = deque([(1,0,0)])
  while(q):
    t,x,y = q.popleft()
    for a,b in d:
      nt = t+1
      nx = x+a
      ny = y+b
      if n>nx>=0 and m>ny>=0 and g[nx][ny] == '1':
        q.append((nt,nx,ny))
        g[nx][ny] = 0
      if nx == (n-1) and ny == (m-1):
        return nt

print(bfs())