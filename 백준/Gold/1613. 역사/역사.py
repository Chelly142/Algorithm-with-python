import sys
from collections import deque
input = sys.stdin.readline
#11:50
n, k = map(int,input().split())
# d_past ={i:set() for i in range(1,n+1)}
# d_future ={i:set() for i in range(1,n+1)}
g = [[0]*(n+1) for _ in range(n+1)]
for _ in range(k):
    p,f = map(int,input().split())
    g[p][f] = -1
    g[f][p] = 1
    # d_past[f].add(p)
    # d_future[p].add(f)
s = int(input())
case = [tuple(map(int,input().split())) for _ in range(s)]

# def bfs(start,end):
#     q = deque([start])
#     while q:
#         now = q.popleft()
#         if now==end:
#             return -1
#         for next in d_back[now]:
#             d_back[start].add(next)
#             q.append(next)
#     q = deque([start])
#     while q:
#         now = q.popleft()
#         if now==end:
#             return 1
#         for next in d_front[now]:
#             d_front[start].add(next)
#             q.append(next)
#     return 0
# answer =[]
# def dfs_past(start,end,now):
#     if now ==end:
#         return 1
#     for next in list(d_past[now]):
#         d_past[start].add(next)
#         if dfs_past(start,end,next)==1:
#             return 1
#     return 0
# def dfs_future(start,end,now):
#     if now ==end:
#         return -1
#     for next in list(d_future[now]):
#         d_future[start].add(next)
#         if dfs_future(start,end,next)==-1:
#             return -1
#     return 0

# def check(start,end):
#     past = dfs_past(start,end,start)
#     future = dfs_future(start,end,start)
#     if past ==1:
#         return past
#     if future ==-1:
#         return -1
#     return 0
 


for m in range(1,n+1):
    for s in range(1,n+1):
        for e in range(1,n+1):
            if g[s][m]==-1 and g[m][e]==-1:
                g[s][e] = -1
                g[e][s] = 1
for x,y in case:
    print(g[x][y])
#12:18 메모리 초과 bfs
#12:55 시간 초과 dfs
#13:13 시간 초과 플루이드 워셜