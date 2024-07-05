import sys
input = sys.stdin.readline
n,m = map(int,input().split())
# n = int(input())
def k(x,y):
    if x> 1000:
        return k(min(x,y),max(x,y)%min(x,y))
    i=min(x,y)
    while i>1:
        if x%i==0 and y%i==0:
            return i
        else:
            i-=1
    return 1

print(n*m//k(n,m))
    