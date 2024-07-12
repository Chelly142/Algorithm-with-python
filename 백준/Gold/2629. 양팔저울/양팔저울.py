import sys
input = sys.stdin.readline

# dp[i][j] = min(dp[i][t]+dp[t+1][j]+row[i]*col[t]*col[j] for t in range(i,j))

n = int(input())
chu = [0]+list(map(int,input().split()))
t = int(input())
cases = list(map(int,input().split()))
s =sum(chu)

dp = [[False]*(s+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,s+1):
        if chu[i]>=j:
            dp[i][j] = dp[i-1][chu[i]-j] or dp[i-1][j] or chu[i]==j
        if chu[i]+j<=s:
            dp[i][j] = dp[i][j] or dp[i-1][chu[i]+j]
        dp[i][j] = dp[i][j] or dp[i-1][j] or dp[i-1][j-chu[i]] 
answer =""
for i in cases:
    if i>s:
        answer+="N "
    elif dp[-1][i]:
        answer+="Y "
    else:
        answer+="N "
print(answer)