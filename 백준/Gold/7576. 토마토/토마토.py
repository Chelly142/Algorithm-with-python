from collections import deque
m,n = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

d = [(1,0),(0,1),(-1,0),(0,-1)]
def bfs(g):
  l=[]
  cnt=0
  answer=0
  for i in range(m):
    for j  in range(n):
      if g[j][i] == 1 :
        l.append((j,i))
        cnt+=1

  q = deque(l)
  while q:
    if cnt == 0:
      cnt=len(q)
      answer+=1
    a = q.popleft()
    cnt-=1
    for i in d:
      x = a[0]+i[0]
      y=  a[1]+i[1]
      if n>x>=0 and m>y>=0 and g[x][y]==0:
        q.append((x,y))
        g[x][y] = 1
  for i in g:
    for j in i:
      if j == 0:
        answer = -1
  return(answer)
print(bfs(graph))