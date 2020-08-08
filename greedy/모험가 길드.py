from collections import deque

n = int(input())
l = list(map(int,input().split()))
l.sort()

que = deque(l)
c = 0
t = 1
while que:
    v = que.popleft()
    if t!=v:
        t += 1
    else:
        t = 1
        c+=1
    
print(c)
