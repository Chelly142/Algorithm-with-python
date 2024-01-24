#3:44
n,m,v = map(int,input().split())
g = []
for i in range(m):
  g.append(list(map(int,input().split())))
for i in g:
  if i[0]>i[1]:
    i[0],i[1] = i[1],i[0]
g.sort()
visited_dfs = [v]
visited_bfs = [v]

def dfs(t):
  
  for i in g:
    if i[0]==t and i[1] not in visited_dfs:
      visited_dfs.append(i[1])
      dfs(i[1])
    elif i[1]==t and i[0] not in visited_dfs:
      visited_dfs.append(i[0])
      dfs(i[0])


def bfs(t):
  q = [t]
  while q:
    c = q.pop(0)
    for i in g:
      if i[0]==c and i[1] not in visited_bfs:
        q.append(i[1])
        visited_bfs.append(i[1])
      elif i[1]==c and i[0] not in visited_bfs:
        q.append(i[0])
        visited_bfs.append(i[0])
       

dfs(v)
bfs(v)

print(*visited_dfs)
print(*visited_bfs)