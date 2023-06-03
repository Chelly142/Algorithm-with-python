
r , c = map(int,input().split())
g = [list(input()) for _ in range(r)]
direction = [(1,0),(0,1),(-1,0),(0,-1)]
answer = 1
def dfs(x,y,visit):
  global answer
  for d in direction:
    nx = x+d[0]
    ny = y+d[1]
    if r>nx>=0 and c>ny>=0 and g[nx][ny] not in visit:
      dfs(nx,ny,visit+g[nx][ny])
    answer = max(answer, len(visit))
      
dfs(0,0,g[0][0])
print(answer)