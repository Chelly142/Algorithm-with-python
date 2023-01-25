n, m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))
result =0
def dfs(x, y):
    if x>=n or x<0 or y>=m or y<0:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1

print(result)
'''
n,m = map(int,input().split())
graph = []
for i in range(n):
  graph.append(list(map(int,input())))

def dfs(g,x,y):
  g[x][y] = 1
  if (x+1)!=n and g[x+1][y] == 0:
    x = x+1
    dfs(g,x,y)
  if (y+1)!=m and g[x][y+1] == 0:
    y = y+1
    dfs(g,x,y)
  if(x-1)>=0 and g[x-1][y] == 0:
    x = x-1
    dfs(g,x,y)
  if(y-1)>=0 and g[x][y-1] == 0:
    y = y-1
    dfs(g,x,y)
cnt = 0
for i in range(n):
  for j in range(m):
    if graph[i][j] == 0:
      dfs(graph,i,j) 
      cnt+=1
print(cnt)'''