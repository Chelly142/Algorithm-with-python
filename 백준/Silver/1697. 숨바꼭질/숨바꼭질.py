#3:08
# 가고자 하는 노드 xd에 대해
#x = min(x/2,x-1,x+1) 짝수 의경우
#x = min(x-1,x+1) 홀 수의 경우
# bfs?
from collections import deque

def bfs(g,start, end):
  q = deque([start])

  while q:
    now_node = q.popleft()
    if now_node ==end:
      return g[now_node]
    if now_node-1>=0 and g[now_node-1]==0:
      q.append(now_node-1)
      g[now_node-1] = g[now_node] + 1
    if 100000>=now_node+1 and g[now_node+1]==0:
      q.append(now_node+1)
      g[now_node+1] = g[now_node] + 1
    if 100000>=now_node*2 and g[now_node*2]==0:
      q.append(now_node*2)
      g[now_node*2] = g[now_node] + 1
graph = [0]*100001
s,e = map(int,input().split())
print(bfs(graph,s,e))