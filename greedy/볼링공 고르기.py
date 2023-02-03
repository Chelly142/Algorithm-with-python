n, m = map(int,input().split())
l = list(map(int,input().split()))
a =[]
for i in range(1,m+1):
    a.append(l.count(i))
k = 0
for i in a:
    k += i*(i-1)/2
result = n*(n-1)/2 -k

print(int(result))

n,m = map(int,input().split())
l = list(map(int,input().split()))
c = [0]*m

d=0
for i in range(1,m+1):
  a = l.count(i)
  d+=a*(a-1)/2
s = set(l)
print(int(len(l)*(len(l)-1)/2 - d))
