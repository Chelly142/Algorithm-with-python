n, m = map(int, input().split())
k = []
for i in range(n):
    l = list(map(int,input().split()))
    k.append(min(l))
print(max(k))

'''
n,m = map(int,input().split())
result = 0
for i in range(n):
  list = map(int, input().split())
  a = min(list)
  if (result < a):
    result = a
print(result)
'''