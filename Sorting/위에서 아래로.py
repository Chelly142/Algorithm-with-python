n = int(input())
k=[]
for i in range(n):
    k.append(input())
k.sort(reverse =True)
print(' '.join(k))
