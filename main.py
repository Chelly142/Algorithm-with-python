n,m = map(int,input().split())
graph = []
for i in range(n):
  graph.append(list(map(int,input())))

def dfs(graph,x,y):
  if graph[x][y]==0:
    graph
    