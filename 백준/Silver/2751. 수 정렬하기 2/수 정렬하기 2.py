import sys
input = sys.stdin.readline
n = int(input())
# n, k= map(int, input().split())
l =[]
for i in range(n):
    l.append(int(input()))

for i in sorted(l):
    print(i)       
         
                    

                        