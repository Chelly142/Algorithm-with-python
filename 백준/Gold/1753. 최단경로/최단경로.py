#11:56
import heapq
INF = int(1e9)
v ,e = map(int, input().split())
k = int(input())
d = [INF]*(v+1) 
d[k] = 0
g = {}
for i in range(v+1):
  g[i] = []
for _ in range(e):
  x,y,l = map(int,input().split())
  g[x].append((l,y))
  
q=[]
heapq.heappush(q,(0,k))
while q:
  now_d, node = heapq.heappop(q)
  if d[node] < now_d:
    continue
  
  for  distance,target_node in g[node]:
    if distance+now_d <d[target_node]:
      d[target_node] = distance+now_d
      heapq.heappush(q,(distance+now_d, target_node))

for i in range(1,v+1):
  if d[i]==INF:
    print("INF")
  else:
    print(d[i])
