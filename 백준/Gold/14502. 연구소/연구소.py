#1:15
from itertools import combinations
from collections import deque
from copy import deepcopy
n,m = map(int,input().split())
g = [list(map(int,input().split())) for _ in range(n)]

void = []
virus = []
for i in range(n):
  for j in range(m):
    if g[i][j] == 0:
      void.append((i,j))
    if g[i][j] == 2:
      virus.append((i,j))
combi = combinations(void,3)
directions = [(1,0),(0,1),(-1,0),(0,-1)]
def bfs(graph):
  for v in virus:
    q = deque([v])
    while q:
      now_node = q.popleft()
      for d in directions:
        nx = now_node[0] + d[0]
        ny = now_node[1] + d[1]
        if n>nx>=0 and m>ny>=0 and graph[nx][ny]==0 :
          graph[nx][ny] = 2
          q.append((nx,ny))
  count = 0
  for i in graph:
    for j in i:
      if j == 0:
        count+=1
  return count
answer =0
for i in combi:
  temp = deepcopy(g)
  for j in i:
    temp[j[0]][j[1]] = 1
  answer = max(answer,bfs(temp))
print(answer)