import sys
sys.setrecursionlimit(111111)
input = sys.stdin.readline

#13:10
n = int(input())

graph = [input() for _ in range(n)]

visited = []

def dfs(now_node):
    visited.append(now_node)
    for i in range(n):
      if graph[now_node][i]=='Y' and i not in visited:
            dfs(i)

connected_graph_cnt =0
edge_cnt = 0
island = False
for i in range(n):
      if "Y" not in graph[i]:
           island =True
           break
      edge_cnt+=graph[i].count("Y")
      if i not in visited:
            connected_graph_cnt+=1
            dfs(i)

if n==1:
     print(0)
elif edge_cnt//2<n-1 or island:
     print(-1)
else:
     print(connected_graph_cnt-1)
