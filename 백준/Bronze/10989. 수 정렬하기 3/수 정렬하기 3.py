import sys
input = sys.stdin.readline
n = int(input())
# n, k= map(int, input().split())
l = {i:0 for i in range(1,10001)}


for _ in range(n):
    l[int(input())]+=1


for i in range(1,10001):
    if l[i]==0:
        continue
    else:
        for j in range(l[i]):
            print(i)       
         
                    

                        