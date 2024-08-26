from collections import deque
import sys
input = sys.stdin.readline

x = int(input())
INF = 10e9
dp = [INF]*(x+1)

dp[1] = 0
now_num = 1
q=deque([1])
while q:
    now_num=q.popleft()
    if now_num==x:
        break
    if now_num+1<=x and dp[now_num+1]==INF:
        dp[now_num+1] = now_num
        q.append(now_num+1)
    if now_num*2<=x and dp[now_num*2]==INF:
        dp[now_num*2] = now_num
        q.append(now_num*2)
    if now_num*3<=x and dp[now_num*3]==INF:
        dp[now_num*3] = now_num
        q.append(now_num*3)

answer = []
n=x
while n!=0:
    answer.append(n)
    n = dp[n]
print(len(answer)-1)
print(*answer)