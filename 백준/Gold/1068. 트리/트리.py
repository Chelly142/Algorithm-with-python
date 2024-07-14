import sys
import copy
from collections import deque
input = sys.stdin.readline
#13:40
# 두 단계
# 1 노드가 지워진 트리 구축
# 2 리프 count

n = int(input())
tree = list(map(int,input().split()))
del_n = int(input())
root = -1
d ={i:set() for i in range(n)}
for i in range(len(tree)):
    if tree[i] == -1:
        root = i
    if i == del_n:
        continue
    if tree[i] != -1:
        d[tree[i]].add(i)
    

q = deque([root])
answer = 0

if root!= del_n:
    while q:
        now = q.popleft()
        if len(d[now])==0:
            answer+=1
        for next in d[now]:
            q.append(next)

print(answer)