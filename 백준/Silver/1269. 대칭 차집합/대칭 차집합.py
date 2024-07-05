import sys
input = sys.stdin.readline
n,m = map(int,input().split())
# n = int(input())

a = {}
for i in map(int,input().split()):
    a[i]=0
b = {}
for i in map(int,input().split()):
    b[i]=0
answer = len(a)+len(b)
for i in a:
    if i in b:
        answer-=2

print(answer)
              

                        