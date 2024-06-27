def solution(temperature, t1, t2, a, b, onboard):
    answer = 0
    temperature+=10
    t1+=10
    t2+=10
    dp = [[1e9]*51 for _ in range(len(onboard))]
    dp[0][temperature]=0
    for i in range(1,len(onboard)):
        for j in range(51):
            if onboard[i]==0 or t1<=j<=t2:
                if 0<=j-1 < temperature:
                    dp[i][j] = min(dp[i][j],dp[i-1][j-1])
                if 51>j+1 > temperature:
                    dp[i][j] = min(dp[i][j],dp[i-1][j+1])
                if j == temperature:
                    dp[i][j] = min(dp[i][j],dp[i-1][j])
                if j-1>=0:
                    dp[i][j] = min(dp[i][j],dp[i-1][j-1]+a)
                if 51>j+1:
                    dp[i][j] = min(dp[i][j],dp[i-1][j+1]+a)
                dp[i][j] = min(dp[i][j],dp[i-1][j]+b)
    return min(dp[-1])