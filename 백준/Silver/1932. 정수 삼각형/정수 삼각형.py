#바텀업
n = int(input())
g =[]
for i in range(n):
  g.append(list(map(int,input().split())))

memo = [g[0]]
for i in range(1,n):
  l=[0]*(i+1)
  for j in range(i+1):
    if j==0:
      l[j] = g[i][j]+memo[i-1][j]
    elif j==i:
      l[j] = g[i][j]+memo[i-1][j-1]
    else:
      l[j] = g[i][j]+max(memo[i-1][j-1],memo[i-1][j])
  memo.append(l)
print(max(memo[-1]))
