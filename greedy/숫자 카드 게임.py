n, m = map(int, input().split())
k = []
for i in range(n):
    l = list(map(int,input().split()))
    k.append(min(l))
print(max(k))
