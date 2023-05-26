#5:17
n, m = map(int,input().split())
kb = [[100]*(n+1) for _ in range(n+1)]

for i in range(n+1):
  kb[i][0] = 0
  kb[i][i] = 0
for _ in range(m):
  x,y = map(int,input().split())
  kb[x][y] = 1
  kb[y][x] = 1

for i in range(1,n+1):
  for j in range(1,n+1):
    for k in range(1,n+1):
      if kb[j][k] > kb[j][i] + kb[i][k]:
         kb[j][k] = kb[j][i] + kb[i][k]
a =1000000
for i in range(1,n+1):
  if a > sum(kb[i]):
    answer = i
    a = sum(kb[i])
print(answer)