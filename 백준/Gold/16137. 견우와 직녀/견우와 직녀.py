import sys
from collections import deque
import heapq
input = sys.stdin.readline

#16:41
n, m =map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]


dxs =(0,0,1,-1)
dys =(1,-1,0,0)
def is_range(x,y):
    return 0<=x<n and 0<=y<n
def is_bridge_possible(x,y):
    row =False
    col=False
    for dx, dy in zip(dxs,dys):
        if is_range(x+dx,y+dy):
            if graph[x+dx][y+dy]!=1:
                if dx!=0:
                    row = True
                if dy!=0:
                    col = True
    return (not row or not col) and graph[x][y]==0

new_bridges=[] # 새로운 다리
bridges={i:[] for i in range(21)} # 원래 있던 다리
for x in range(n):
    for y in range(n):
        if is_bridge_possible(x,y):
            new_bridges.append((x,y))
        if graph[x][y]>=2:
            bridges[graph[x][y]].append((x,y))



answer = 10e9


for new_bridge_x, new_bridge_y in new_bridges:
    graph[new_bridge_x][new_bridge_y] = m
    can_bridge = True
    q = [(0,0,0,True)] # 시각, x, y
    visited =set((0,0))
    # print(new_bridge_x, new_bridge_y)
    while q:
        t,x,y,can_bridge = heapq.heappop(q)
        # print(t,x,y,True)
        if x==n-1 and y==n-1:
            answer = min(answer,t)
            break
        for dx,dy in zip(dxs,dys):
            next_x, next_y = x+dx, y+dy
            if is_range(next_x,next_y) and (next_x,next_y) not in visited:
                if graph[next_x][next_y]==1: # 다음 그냥 땅으로 가는 경우
                    heapq.heappush(q,(t+1,next_x,next_y,True))
                    visited.add((next_x,next_y))
                if graph[next_x][next_y]>=2: # 다음 오작교로 가는 경우
                    if can_bridge: #이전에 땅에서 온 경우
                        heapq.heappush(q,(t+graph[next_x][next_y]-t%graph[next_x][next_y],next_x,next_y,False))
                        visited.add((next_x,next_y))

                
    graph[new_bridge_x][new_bridge_y] = 0
    
print(answer)


