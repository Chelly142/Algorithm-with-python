import sys
import copy
sys.setrecursionlimit(10**7)

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))
def rain(d,g):
  answer = 0
  for i in range(n):
    for j in range(n):
      if g[i][j]<=d:
        g[i][j] = 0
  def dfs(x,y):
    g[x][y] = 0
    if x+1<n and g[x+1][y]!=0:
      dfs(x+1,y)
    if x-1>=0 and g[x-1][y]!=0:
      dfs(x-1,y)
    if y+1<n and g[x][y+1]!=0:
      dfs(x,y+1)
    if y-1>=0 and g[x][y-1]!=0:
      dfs(x,y-1)
  for i in range(n):
    for j in range(n):
      if g[i][j] !=0 :
        dfs(i,j)
        answer+=1
  return answer
b =[]
for i in range(0,101):
  a = rain(i,copy.deepcopy(graph))
  if a == 0:
    b.append(0)
    break
  else:
    b.append(a)


print(max(b))
