import sys
input = sys.stdin.readline
n,m = map(int,input().split())
# n = int(input())
d1 = {}
d2 = {}
for i in range(n):
    x = input().rstrip()
    d1[x]=i+1
    d2[i+1]=x

l = {str(i):0 for i in range(1,100001)}
answer =[]
for i in range(m):
    x = input().rstrip()
    if x in l:
        answer.append(d2[int(x)])
        
    else:
        answer.append(d1[x])
for i in answer:
    print(i)                    

                        