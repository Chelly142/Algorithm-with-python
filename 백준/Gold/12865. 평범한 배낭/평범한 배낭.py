import sys
input = sys.stdin.readline

# dp[i] = max(dp[i-1], dp[k-weights[i]]+values[i])



n, k = map(int,input().split())

arr = [(0, 0)]
dp = [[0] * (k + 1) for _ in range(n + 1)]
for _ in range(n):
    w, v = map(int, input().split())
    arr.append((w, v))
for i in range(1,n+1):
    w, v = arr[i]
    for j in range(1,k+1):
        if w<=j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)
        else:
            dp[i][j] = dp[i-1][j]
print(dp[-1][-1])