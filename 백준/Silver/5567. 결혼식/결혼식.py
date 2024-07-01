#2:27
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
relationships = {}
for i in range(n+1):
    relationships[i] = []
for m in range(m):
    x,y = map(int,input().split())
    relationships[x].append(y)
    relationships[y].append(x)

attend_f = set([])
answer = 0

def bfs():
    global answer
    q = deque([(1,0)])
    while q:
        now_f, d= q.popleft() #현재 친구, 관계 깊이
        attend_f.add(now_f)
        if d!=2:
            for next_f in relationships[now_f]:
                q.append((next_f,d+1))
bfs()
answer = attend_f.__len__()-1
print(answer)