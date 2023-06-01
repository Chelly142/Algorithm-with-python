from collections import deque

m,n,h = map(int,input().split())
g=[]
for _ in range(h):
  box =[]
  for _ in range(n):
    box.append(list(map(int,input().split())))
  g.append(box)

start_tomato =[]
for i in range(h):
  for j in range(n):
    for k in range(m):
      if g[i][j][k] == 1:
        start_tomato.append((0,i,j,k))
direction = [(1,0,0),(0,1,0),(0,0,1),(-1,0,0),(0,-1,0),(0,0,-1)]

def is_void():
  for i in range(h):
    for j in range(n):
      for k in range(m):
        if g[i][j][k] == 0:
          return True
def bfs():
  q = deque(start_tomato)
  while q:
    now_node = q.popleft()
    nt = now_node[0]
    t = nt
    nh = now_node[1]
    nx = now_node[2]
    ny = now_node[3]
    for d in direction:
      next_h = nh+d[0]
      next_x = nx+d[1]
      next_y = ny+d[2]
      if h>next_h>=0 and n>next_x>=0 and m>next_y>=0 and g[next_h][next_x][next_y]==0:
        g[next_h][next_x][next_y] = 1
        q.append((nt+1,next_h,next_x,next_y))
  if is_void():
    return -1
  return t
print(bfs())    