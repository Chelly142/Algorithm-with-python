from collections import deque
#10:17
n = int(input())
a,b = map(int,input().split())
m = int(input())
g = [tuple(map(int,input().split())) for _ in range(m)]

def bfs(s,e):

  q = deque([s])
  tq = deque([0])
  v = [0]*m
  while q:
    n = q.popleft()
    t = tq.popleft()
    for i in range(m):
      if v[i]==0 and g[i][0] == n:
        if g[i][1] == e:
          return t+1
        v[i] = 1
        q.append(g[i][1])
        tq.append(t+1)
      if v[i]==0 and g[i][1] == n:
        if g[i][0] == e:
          return t+1
        q.append(g[i][0])
        tq.append(t+1)
        
  return -1
print(bfs(a,b))