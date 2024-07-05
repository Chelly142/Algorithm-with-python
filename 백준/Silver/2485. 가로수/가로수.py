import sys
input = sys.stdin.readline
# n,m = map(int,input().split())
n = int(input())
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

for _ in range(n):
    l.append(int(input()))
s=set()
for i in range(len(l)-1):
    s.add(l[i+1]-l[i])
s=list(s)
t = s[0]
for i in range(1,len(s)):
    t = k(t,s[i])
answer=0
for i in range(len(l)-1):
    answer+=(l[i+1]-l[i])//t-1
print(answer)