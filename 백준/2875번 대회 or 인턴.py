n, m, k = map(int,input().split())
while k:
    if (2*m)<=n:
        n -= 1
        k -= 1
    else:
        m -= 1
        k -= 1
print(min(m,n//2))
