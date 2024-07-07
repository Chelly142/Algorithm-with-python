import sys
from collections import deque
input = sys.stdin.readline
#3:23
#본인보다 작은 사람 수 + 본인보다 큰 사람 수 = n-1 이면 True
n,m = map(int,input().split())
larger = {i:[] for i in range(n+1)} #g[i] 안에 있는 놈들은 i보다 큰 녀석들
smaller = {i:[] for i in range(n+1)} #g[i] 안에 있는 놈들은 i보다 작은 녀석들
for i in range(m):
    a,b = map(int, input().split())
    larger[a].append(b)
    smaller[b].append(a)
#중복 연산 발생 여지 생김
#일단 bfs로 
def check(x):
    q = deque([])
    q.append(x)
    v_l = [False]*(n+1)
    v_s = [False]*(n+1)
    c_l=0
    c_s=0
    while q:
        now = deque.popleft(q)
        for next in larger[now]:
            if not v_l[next]:
                q.append(next)
                v_l[next] = True
                c_l+=1
    q.append(x)
    while q:
        now = deque.popleft(q)
        for next in smaller[now]:
            if not v_s[next]:
                q.append(next)
                v_s[next] = True
                c_s+=1  
    if c_s+c_l==n-1:
        return True
    return False
        
# 3:57 시간초과

answer = 0

for i in range(1,n+1):
    if check(i):
        answer +=1
print(answer)