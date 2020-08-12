import heapq
import sys
input = sys.stdin.readline


INF = int(1e9)
n, m ,c = map(int,input().split())
graph = [[] for i in range(n+1)]
d = [INF]*(n+1)
for _ in range(m):
    x, y, z = map(int,input().split())
    graph[x].append((y,z))
q = []
heapq.heappush(q,(0,c))
d[c] = 0
while q:
    dist, now = heapq.heappop(q)
    if d[now] < dist:
        comtinue
    for i in graph[now]:
        cost = i[1] + dist
        if cost < d[i[0]]:
            d[i[0]] = cost
            heapq.heappush(q,(cost,i[0]))

city_count =0
time = 0
for i in d:
    if i!=INF:
        city_count+=1
        if time<i:
            time = i
print(city_count-1,end =' ')
print(time)
# 줜나 어려우니 다시 풀것
