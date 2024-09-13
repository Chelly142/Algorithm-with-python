from collections import deque 
n, x = map(int, input().split())
INF = 10e9
dp = [[INF, -1] for _ in range(100001)]
dp[n] = [0,-1]
q = deque([n])
while q:
    now_node = q.popleft()
    if now_node==x:
        break
    if now_node+1<100001 and dp[now_node+1][0]==INF:
        dp[now_node+1] = [dp[now_node][0]+1,now_node]
        q.append(now_node+1)
    if now_node-1 >= 0 and dp[now_node-1][0]==INF:
        dp[now_node-1] = [dp[now_node][0]+1,now_node]
        q.append(now_node-1)
    if now_node*2 <100001 and dp[now_node*2][0]==INF:
        dp[now_node*2] = [dp[now_node][0]+1,now_node]
        q.append(now_node*2)

path = [x]
now_node = x
while len(path) <= dp[x][0]:
    now_node = dp[now_node][1]
    path.append(now_node)
print(dp[x][0])
print(*(path[::-1]))