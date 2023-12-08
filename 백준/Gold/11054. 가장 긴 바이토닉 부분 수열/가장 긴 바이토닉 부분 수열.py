n = int(input())
a = list(map(int,input().split()))

right = [[0,0] for _ in range(n)]
left = [1]*n
right = [1]*n
for i in range(n):
  for j in range(i+1,n):
    if a[i] <a[j]:
      left[j] = max(left[i] + 1, left[j])
for i in range(n-1,-1,-1):
  for j in range(i,-1,-1):
    if a[i] <a[j]:
      right[j] = max(right[i] + 1, right[j])
s=0
for i in range(n):
    s= max(s,left[i]+right[i])
print(s-1)
