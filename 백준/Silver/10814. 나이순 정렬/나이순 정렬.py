import sys
input = sys.stdin.readline
n = int(input())
l=[]
for _ in range(n):
    x,y = input().split()
    l.append((int(x),y))
l.sort(key= lambda x:x[0])
for i in l:
    print(str(i[0])+" "+i[1])


                    

                        