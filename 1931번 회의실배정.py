from collections import deque

n = int(input())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
l = sorted(l,key = lambda x:(x[1],x[0]))
que = deque(l)
c=0
s=0
while que:
    v = que.popleft()
    if s<=v[0]:
        s = v[1]
        c+=1
print(c)
# 생각 난대로 하지말고 더 효율적인 방식 고려하기
