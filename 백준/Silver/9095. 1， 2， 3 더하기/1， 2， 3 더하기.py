#가장 왼쪽에 1이오는 경우 2가오는 경우 3이 오는 경우

t = int(input())
ns = []
for i in range(t):
  ns.append(int(input()))
l = [0]*11
l[1] = 1
l[2] = 2
l[3] = 4
n = max(ns)
for i in range(1,n+1):
  if i>3:
    l[i] = l[i-1]+l[i-2]+l[i-3]

for i in ns:
  print(l[i])

