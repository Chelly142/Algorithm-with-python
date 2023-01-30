n,m = 7,12
g = [(3,1,2),(2,3,1),(1,2,3),(2,5,2),(4,4,3),(6,3,7),(5,1,5),(2,6,1),(1,4,6),(3,5,6),(3,5,4),(4,7,6)]

def find_parent(parent,x):
  if parent[x]!=x:
    parent[x] = find_parent(parent,parent[x])
  return parent[x]
def union_parent(parent, a,b):
  a = find_parent(parent,a)
  b = find_parent(parent,b)
  if a<b:
    parent[b] = a
  else:
    parent[a] = b
parent = [0]*(n+1)
result =0
mx=0
g.sort()
for i in range(0,n+1):
  parent[i] = i
for i in g:
  a = i[1]
  b = i[2]

  if find_parent(parent,a) != find_parent(parent, b):
    union_parent(parent,a,b)
    result+=i[0]
    mx = max(i[0],mx)
print(result-mx)
