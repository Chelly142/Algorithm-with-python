import sys
input = sys.stdin.readline
# n,m = map(int,input().split())
n = int(input())
def m(x,y):
    i=min(x,y)
    while i>1:
        if x%i==0 and y%i==0:
            return x*y//i
        else:
            i-=1
    return x*y

answer = []
for _ in range(n):
    a,b = map(int,input().split())
    answer.append(m(a,b))

for i in answer:
    print(i)
    