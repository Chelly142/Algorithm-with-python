import sys
input = sys.stdin.readline
n,m = map(int,input().split())
d = {}
s=0
for i in range(n):
    x = input()
    d[x]=0
for j in range(m):
    x = input()
    if x in d:
        s+=1
print(s)

                    

                        