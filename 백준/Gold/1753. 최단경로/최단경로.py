import heapq
v, e = map(int,input().split())
k = int(input())
g =[[] for _ in range(v+1)]
INF = 10e9
for _ in range(e):
  a,b,d = map(int,input().split())
  g[a].append((b,d))
d=[INF]*(v+1)
d[k] = 0
q=[(0,k)]
while q:
  dist, now = heapq.heappop(q)
  if dist>d[now]:
    continue
  for i in g[now]:
    c = dist+i[1]
    if c<d[i[0]]:
      d[i[0]] = c
      q.append((c,i[0]))
for i in range(1,v+1):
  if d[i] == INF:
    print("INF")
  else:
    print(d[i])