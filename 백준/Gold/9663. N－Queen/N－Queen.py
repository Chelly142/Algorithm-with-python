

n = int(input())

answer = 0

def promising(g,i):
  if i in g:
    return False
  for j,v in enumerate(g):
    if abs(len(g)-j) == abs(i-v):
        return False
  return True
def dfs(g):
  global answer
  if len(g) == n:
    answer += 1
  for i in range(n):
    if promising(g,i):
      t = g[:]
      t.append(i)
      dfs(t)

for i in range(n):
  dfs([i])

print(answer)
