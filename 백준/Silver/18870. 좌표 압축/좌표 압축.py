import sys
input = sys.stdin.readline
n = int(input())
l= list(map(int,input().split()))
l_d = l[:]

k={}
j=0
for i in sorted(set(l_d)):
    k[i] = j
    j+=1
if n==1:
    print(0)  
else:  
    for i in l:
        print(k[i],end=" ")


                    

                        