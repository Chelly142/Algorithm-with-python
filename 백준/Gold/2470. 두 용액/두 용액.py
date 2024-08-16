import sys
input = sys.stdin.readline

n =int(input())
a = list(map(int,input().split()))
a.sort()
front = 0
back = n-1
answer=(a[0],a[n-1])
close_0 = abs(a[0]+a[n-1])

while front<back:
    if abs(a[front]+a[back])<close_0:
        answer=(a[front],a[back])
        close_0 = abs(a[front]+a[back])
    if a[front]+a[back]==0:
        break
    elif a[front]+a[back]<0:
        front+=1
    elif a[front]+a[back]>0:
        back-=1
print(*answer)