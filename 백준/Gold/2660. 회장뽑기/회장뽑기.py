#2:58
import sys
from collections import deque
input = sys.stdin.readline

#가장 먼 관계가 본인 점수
#입력 작다 회원 당 고려

n = int(input())
relationships = {i:set() for i in range(n+1)}
while True:
    a,b = map(int,input().split())
    if a==-1 and b==-1:
        break
    else:
        relationships[a].add(b)
        relationships[b].add(a)


def score(k):
    q = deque([(k,0)])
    d = 0
    visited = [False]*(n+1)
    visited[k] = True
    while q:
        now_f, d = q.popleft() # 현재 친구, 관계 깊이 
        
        for next_f in relationships[now_f]:
            if not visited[next_f]:
                q.append((next_f,d+1))
                visited[next_f] = True
    return d
scores = []
for f in range(1,n+1):
    scores.append(score(f))
m = min(scores)

print(m, scores.count(m))
for i,v in enumerate(scores):
    if v == m:
        print(i+1,end=" ")