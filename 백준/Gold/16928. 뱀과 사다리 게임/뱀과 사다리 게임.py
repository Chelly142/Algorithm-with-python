import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = {i:[i+j for j in range(1,7) if i+j<=100] for i in range(1,101)}

ladders = {}
snakes = {}
for i in range(n):
    start, end = map(int,input().split())
    ladders[start] = end
for i in range(m):
    start, end = map(int,input().split())
    snakes[start] = end

q = deque([(1,0)])
answer = 0
visited = set()
while q:
    now_node, now_times = q.popleft()
    if now_node>=100:
        answer = now_times
        break

    for next_node in graph[now_node]:
        if next_node in visited:
            continue
        if next_node in snakes:
            visited.add(snakes[next_node])
            q.append((snakes[next_node],now_times+1))
        elif next_node in ladders:
            visited.add(ladders[next_node])
            q.append((ladders[next_node],now_times+1))
        else:
            visited.add(next_node)
            q.append((next_node, now_times+1))

            
print(answer)