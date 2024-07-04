import sys
input = sys.stdin.readline
n,m = map(int,input().split())
# n = int(input())

d = {}
answer = []
for i in range(n):
    x = input()
    d[x] = 0
for j in range(m):
    x = input()
    if x in d:
        answer.append(x)
print(len(answer))
for i in sorted(answer):
    print(i,end="")

              

                        