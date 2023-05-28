#2:23
from collections import deque



def bfs(l,start,end):
  q = deque([start])
  g = [[0]*l for _ in range(l)]
  directions = [(2,1),(1,2),(-2,1),(1,-2),(-1,2),(2,-1),(-2,-1),(-1,-2)]

  while q:
    now_node = q.popleft()
    nx = now_node[0]
    ny = now_node[1]
    if now_node == end:
      return g[nx][ny]# 횟수
    for d in directions:
      if l>nx+d[0]>=0 and l>ny+d[1]>=0 and g[nx+d[0]][ny+d[1]] == 0:
        q.append((nx+d[0],ny+d[1]))
        g[nx+d[0]][ny+d[1]] =g[nx][ny]+1
  return 0

answer = []
n = int(input())
for _ in range(n):
  size = int(input())
  s = tuple(map(int,input().split()))
  e = tuple(map(int,input().split()))
  answer.append(bfs(size,s,e))
for i in answer:
  print(i)
  

  
