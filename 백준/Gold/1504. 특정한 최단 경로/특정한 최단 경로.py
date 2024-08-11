import sys
import heapq
input = sys.stdin.readline

n, e = map(int, input().split())
graph = {i:[] for i in range(1,n+1)}
for _ in range(e):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
v1, v2 = map(int, input().split())

def dijkstra(start_node):
    distances = [10e9]*(n+1)
    distances[start_node] = 0
    q = [(0,start_node)]
    while q:
        now_distance, now_node = heapq.heappop(q)
        for nxt_node, edge in graph[now_node]:
            nxt_distance = distances[nxt_node]
            if now_distance+edge<nxt_distance:
                distances[nxt_node] = now_distance+edge
                q.append((distances[nxt_node], nxt_node))
    return distances
dijkstra_1 = dijkstra(1)
dijkstra_v1 = dijkstra(v1)
dijkstra_v2 = dijkstra(v2)
answer = min(dijkstra_1[v1]+dijkstra_v1[v2]+dijkstra_v2[n],dijkstra_1[v2]+dijkstra_v1[v2]+dijkstra_v1[n])
if answer >=10e9: print(-1)
else: print(answer)






