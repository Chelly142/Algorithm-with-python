from bisect import bisect_left

s1 = list(input().rstrip())
s2 = list(input().rstrip())
n = len(s1)
m = len(s2)
dp = [[0]*(m+1) for _ in range(n+1)]
lis = []

for i in range(1,n+1):
    for j in range(1,m+1):
        if s1[i-1]==s2[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])

lcs = dp[n][m]
lcs_str = ""
print(lcs)
i,j = n,m
while i>0 and j>0:
    if s1[i-1]==s2[j-1]:
        lcs_str=s1[i-1]+lcs_str
        i-=1
        j-=1
    elif dp[i][j-1]==dp[i][j]:
        j-=1
    elif dp[i-1][j]==dp[i][j]:
        i-=1
print(lcs_str)