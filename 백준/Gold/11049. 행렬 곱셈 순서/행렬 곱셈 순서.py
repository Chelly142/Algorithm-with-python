import sys
input = sys.stdin.readline

# dp[i][j] = min(dp[i][t]+dp[t+1][j]+row[i]*col[t]*col[j] for t in range(i,j))

n = int(input())
row = []
col = []
for _ in range(n):
    x,y = map(int,input().split())
    row.append(x)
    col.append(y)

dp = [[0]*n for _ in range(n)]

for l in range(2,n+1):
    for i in range(n-l+1):
        dp[i][i+l-1] = min(dp[i][t]+dp[t+1][i+l-1]+row[i]*col[t]*col[i+l-1] for t in range(i,i+l-1))

print(dp[0][-1])