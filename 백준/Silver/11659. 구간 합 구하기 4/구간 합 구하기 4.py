import sys
input = sys.stdin.readline


n, m = map(int,input().split())
l = list(map(int,input().split()))
prefix = [0]
for i in range(n):
    prefix.append(prefix[i]+l[i])

answer =[]
for _ in range(m):
    x,y =map(int,input().split())
    answer.append(prefix[y]-prefix[x-1])
for i in answer:
    print(i)