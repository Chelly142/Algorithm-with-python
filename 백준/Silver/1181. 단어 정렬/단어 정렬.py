import sys
input = sys.stdin.readline
n = int(input())
l=[]
for _ in range(n):
    x =input()
    if x not in l:
        l.append(x)
l.sort()
l.sort(key=lambda x :len(x))
for i in l:
    print(i,end="")


                    

                        