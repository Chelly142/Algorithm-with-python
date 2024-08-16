import sys
import heapq
input = sys.stdin.readline

n =int(input())
a = list(map(int,input().split()))
x =int(input())
a.sort()
front = 0
back = n-1
answer=0
while front<back:
    if a[front]+a[back]==x:
        answer+=1
        front+=1
        back-=1
    if a[front]+a[back]<x:
        front+=1
    if a[front]+a[back]>x:
        back-=1
print(answer)