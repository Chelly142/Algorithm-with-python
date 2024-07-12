import sys
input = sys.stdin.readline

# dp[i][j] = i번째 동전 까지 고려 했을 때 j 가치를 만족하는 모든 경우의 수 
# dp[i][j] = dp[i-1][j]+dp[i][j]+dp[i-1][j-v]
n, k = map(int,input().split())

coins = [int(input()) for _ in range(n)]

dp = [1]+[0]*(k)

for coin in coins:
    for i in range(coin,k+1):
        dp[i] += dp[i-coin]
print(dp[-1])