import sys
input = sys.stdin.readline
# n,m = map(int,input().split())
n = int(input())
d={}
cards = list(map(int,input().split()))

for c in cards:
    if c not in d:
        d[c]=1
    else:
        d[c] += 1

m = int(input())
checks = list(map(int,input().split()))


for i in checks:
    if i not in d:
        print(0,end=" ")
    else:
        print(d[i],end=" ")

              

                        