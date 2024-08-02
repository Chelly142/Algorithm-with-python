import sys
import heapq
input = sys.stdin.readline

n = int(input())

hq = []

for _ in range(n):
    x = int(input()) 
    if x==0:
        if len(hq)==0:
            print(0)
        else:
            a = heapq.heappop(hq)
            print(a[0]*a[1])
    elif x>0:
        heapq.heappush(hq,(x,1))
    elif x<0:
        heapq.heappush(hq,(abs(x),-1))
        