import sys
input = sys.stdin.readline
# n,m = map(int,input().split())
# n = int(input())
l=[]
def k(x,y):
    if max(x,y)%min(x,y)==0:
        return(min(x,y))
    if x> 1000:
        return k(min(x,y),max(x,y)%min(x,y))
    i=min(x,y)
    while i>1:
        if x%i==0 and y%i==0:
            return i
        else:
            i-=1
    return 1

for _ in range(2):
    l.append(tuple(map(int,input().split())))
u=l[0][0]*l[1][1]+l[1][0]*l[0][1]
d=l[0][1]*l[1][1]
t = k(u,d)
print(u//t,d//t)