n,k = map(int,input().split())

w =[]
v= []
for i in range(n):
  x,y= map(int,input().split())
  w.append(x)
  v.append(y)

memo = [[-1]*(k+1) for _ in range(n)]
def dp(i,W):
  if i<0 or W<=0:
    return 0

  if memo[i][W]!=-1:
    return memo[i][W]
  if W>=w[i]:
    memo[i][W] = max(dp(i-1,W-w[i])+v[i],dp(i-1,W))
    return memo[i][W]
  else:
    memo[i][W] = dp(i-1,W)
    return memo[i][W]

print(dp(n-1,k))
