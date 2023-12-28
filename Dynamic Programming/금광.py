# 3:24
#결국 열당 하나 뿐
n,m = map(int,input().split())
l = list(map(int,input().split()))
g=[]
dp=[]
for i in range(n):
  g.append(l[i*m:i*m+m])
for i in range(n):
  dp.append(g[i][0])
print(dp)
print(g)
for i in range(1,m):
  t=[]
  for j in range(n):
    # j j+1 고려
    if j==0:
      t.append(max(dp[0],dp[1])+g[0][i])
    # j j-1  고려  
    elif j==n-1:
      t.append(max(dp[j],dp[n-2])+g[n-1][i])
    # j j-1 j+1 고려
    else:
      t.append(max(dp[j],dp[j+1],dp[j-1])+g[j][i])
  dp= t[0:n]
  print(t)
print(max(dp))
#1 3 3 2 2 1 4 1 0 6 4 7
