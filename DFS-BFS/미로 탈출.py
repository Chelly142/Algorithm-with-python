from collections import deque

n ,m = map(int,input().split())
graph =[]
for i in range(n):
    graph.append(list(map(int,input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(x,y):
    que = deque()
    que.append((x,y))

    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                que.append((nx,ny))
                graph[nx][ny] = graph[x][y]+1
    return graph[n-1][m-1]
print(bfs(0,0))

'''
from collections import deque
n,m = map(int,input().split())
graph = []
for i in range(n):
  graph.append(list(map(int,input())))

x,y = 0,0
q = deque()
q.append((x,y))

while True:
  if q:
   v = q.popleft()
  else:
    break
  if v == (n-1,m-1):
    break
  nx = v[0]
  ny = v[1]
  flag = False
  if nx+1 < n and graph[nx+1][ny]:
    q.append((nx+1,ny))
    graph[nx+1][ny] = graph[nx][ny] + 1

  if ny+1 < m and graph[nx][ny+1]:
    q.append((nx,ny+1))
    graph[nx][ny+1] = graph[nx][ny] + 1

  if nx-1 >= 0  and graph[nx-1][ny]:
    q.append((nx-1,ny))
    graph[nx-1][ny] = graph[nx][ny] + 1

  if ny-1 >= 0 and graph[nx][ny-1]:
    q.append((nx,ny-1))
    graph[nx][ny-1] = graph[nx][ny] + 1

print(graph[n-1][m-1])
'''
