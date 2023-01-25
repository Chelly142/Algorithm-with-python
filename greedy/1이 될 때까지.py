n, k =map(int, input().split())
c=0
while n!=1:
    if n%k == 0:
        n = n/k
        c+=1
    else:
        n -= 1
        c +=1
print(c)

'''
n, k = map(int,input().split())
cnt = 0
while n>=k:
  z = n%k
  if z:
    n = n-z
    cnt = cnt+ z
  else:
    n =n/k
    cnt= cnt+1

print(cnt+n-1)
꽤부리다 더 복잡해졌네
'''
