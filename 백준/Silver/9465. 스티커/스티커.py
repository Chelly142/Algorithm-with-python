t=int(input())
for i in range(t):
  n=int(input())
  g = []
  memo = []
  for i in range(n):
    g.append([0,0])
    memo.append([0,0,0])
  for i in range(2):
    for j,v in enumerate(list(map(int, input().split()))):
      g[j][i] = v
  memo[0] = [0,g[0][0],g[0][1]] 
  for i in range(1,n):
      memo[i][0] = max(memo[i-1])
      memo[i][1] = max(memo[i-1][0],memo[i-1][2])+g[i][0]
      memo[i][2] = max(memo[i-1][0],memo[i-1][1])+g[i][1]
  print(max(memo[n-1]))
  
  
  