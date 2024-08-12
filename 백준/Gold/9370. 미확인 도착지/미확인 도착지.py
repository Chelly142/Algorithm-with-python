import sys
import heapq
input = sys.stdin.readline

T = int(input())

def dijkstra(start_node):
    heap = [(0,start_node)]
    shortest_distance = [10e9]*(n+1)
    shortest_distance[start_node] =0
    while heap:
        now_distance, now_node = heapq.heappop(heap)
        for nxt_node,nxt_distance in enumerate(graph[now_node]):
            if shortest_distance[nxt_node]> now_distance+nxt_distance:
                shortest_distance[nxt_node] =  now_distance+nxt_distance
                heapq.heappush(heap,(shortest_distance[nxt_node], nxt_node))
    return shortest_distance
            
for _ in range(T):
    n,m,t = map(int,input().split())
    s,g,h = map(int,input().split())
    graph = [[10e9]*(n+1) for _ in range(n+1)]
    answer = []
    for _ in range(m):
        a,b,d = map(int,input().split())
        graph[a][b] = d
        graph[b][a] = d
    goal_cases = [int(input()) for _ in range(t)]

    dijkstra_s = dijkstra(s)
    dijkstra_g = dijkstra(g)
    dijkstra_h = dijkstra(h)

    for goal_case in goal_cases:

        if dijkstra_s[h] == dijkstra_s[g]+graph[g][h] and dijkstra_h[goal_case] + dijkstra_s[h] == dijkstra_s[goal_case]:
            answer.append(goal_case)
        elif dijkstra_s[g] == dijkstra_s[h]+graph[h][g] and dijkstra_g[goal_case] + dijkstra_s[g] == dijkstra_s[goal_case]:
            answer.append(goal_case)
    answer.sort()
    print(*answer)



    