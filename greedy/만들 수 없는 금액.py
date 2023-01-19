n = int(input())
l = list(map(int,input().split()))
l.sort()
a=1
t=0
for i in l:
    if t+1<i:
       break
    else:
        t += i
print(t+1)
