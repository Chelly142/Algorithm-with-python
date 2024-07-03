import sys
input = sys.stdin.readline
n = int(input())
d= { i:0 for i in list(map(int,input().split()))}
m = int(input())
k= list(map(int,input().split()))

for i in k:
    if i not in d:
        print(0,end=" ")
    else:
        print(1,end=" ")
                    

                        