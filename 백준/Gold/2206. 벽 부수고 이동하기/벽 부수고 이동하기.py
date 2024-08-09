import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(input().rstrip()) for _ in range(n)]

dxs = [1,-1,0,0]
dys = [0,0,1,-1]

answer = 10e9

def is_range(x,y):
    return 0<=x<n and 0<=y<m

# def dfs(now_x, now_y, now_distance, break_opertunity):
#     global answer
#     if now_x==n-1 and now_y==m-1:
#         answer = min(answer, now_distance)
#         return
#     for dx,dy in zip(dxs,dys):
#         nxt_x, nxt_y = now_x+dx, now_y+dy
#         if is_range(nxt_x,nxt_y) and (nxt_x,nxt_y) not in visited:
#             if graph[nxt_x][nxt_y] =="0":
#                 visited.add((nxt_x,nxt_y))
#                 dfs(nxt_x, nxt_y, now_distance+1, break_opertunity)
#             if graph[nxt_x][nxt_y] =="1" and break_opertunity:
#                 visited.add((nxt_x,nxt_y))
#                 dfs(nxt_x, nxt_y, now_distance+1, not break_opertunity)



break_visited = set()
unbreak_visited = set()
break_visited.add((0,0))
q = deque([(0,0,1,True)])
while q:
    now_x,now_y,now_distance,break_opertunity = q.popleft()
    if now_x==n-1 and now_y==m-1:
        answer = min(answer, now_distance)
        break
    for dx,dy in zip(dxs,dys):
        nxt_x, nxt_y = now_x+dx, now_y+dy
        if is_range(nxt_x,nxt_y):
            if graph[nxt_x][nxt_y] == "1" and break_opertunity:
                break_visited.add((nxt_x,nxt_y))
                q.append((nxt_x, nxt_y, now_distance+1, not break_opertunity))
            if graph[nxt_x][nxt_y] == "0":
                    if break_opertunity and (nxt_x,nxt_y) not in unbreak_visited:
                        unbreak_visited.add((nxt_x,nxt_y))
                        q.append((nxt_x, nxt_y, now_distance+1,break_opertunity))
                    if not break_opertunity and (nxt_x,nxt_y) not in break_visited:
                        break_visited.add((nxt_x,nxt_y))
                        q.append((nxt_x, nxt_y, now_distance+1,break_opertunity))
 


if answer ==10e9: print(-1)
else: print(answer)  