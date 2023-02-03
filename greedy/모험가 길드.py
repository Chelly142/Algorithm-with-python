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

n = int(input())
fears = list(map(int,input().split()))
group = 0
fears.sort()
now_group = 1
for f in fears:
  if f <= now_group:
    group+=1
    now_group = 1
    continue
  now_group+=1
print(group)
