import sys
input = sys.stdin.readline
# n,m = map(int,input().split())
n = int(input())
d = {}
for i in range(n):
    x,y = input().split()
    d[x]=y
answer =[j for j in d if d[j]=="enter"]

for i in sorted(answer,reverse=True):
    print(i)
                    

                        