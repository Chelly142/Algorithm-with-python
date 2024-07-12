import sys
input = sys.stdin.readline


# dp[i] = 
t = int(input())
answer = []


def sum_files(c):
    n = len(c)
    dp = [[0]*n for _ in range(n)]
    for l in range(2,n+1):#부분 파일의 길이
        for i in range(n-l+1):
            dp[i][i+l-1] = min([dp[i][t]+dp[t+1][i+l-1] for t in range(i,i+l-1)]) + sum(c[i:i+l])

    return dp[0][-1]



for _ in range(t):
    k = int(input())
    chapter = list(map(int,input().split()))
    answer.append(sum_files(chapter))


for i in answer:
    print(i)
