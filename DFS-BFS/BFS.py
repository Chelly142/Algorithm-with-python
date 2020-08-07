from collections import deque

def bfs(graph, start, visited):
    visited[start] = True
    que = deque([start])
    while que:
        v = que.popleft()
        print(v,end =' ')
        for i in graph[v]:
            if not visited[i]:
                que.append(graph[i])
                visited[i] =True
