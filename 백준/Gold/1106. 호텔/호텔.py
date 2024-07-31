import sys
input = sys.stdin.readline

# 12:50
c, n = map(int,input().split())
city_cost = [tuple(map(int,input().split())) for _ in range(n)]

#dp 인가?
#배낭 문제인것 같은데?
#중복이 허용되는 배낭문제

# dp row는 고려한 도시
# dp column은 인원 수
# dp[i][j] = min(dp[i-1][j], dp[i-1][j-city_cost[i]])

dp = [[10e9]*(c+1) for _ in range(n+1)]


for i in range(1,n+1):
    cost, people = city_cost[i-1]
    for j in range(1,c+1):
        if j%people==0:
            dp[i][j] = min(dp[i-1][j],(j//people)*cost)
        else:
            dp[i][j] = min(dp[i-1][j],(j//people+1)*cost)
       
        for k in range(people,j,people):
            dp[i][j] = min(dp[i][j],dp[i-1][j-k]+(k//people)*cost)

print(dp[-1][-1])