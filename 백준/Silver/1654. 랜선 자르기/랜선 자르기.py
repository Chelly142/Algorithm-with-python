n , k = map(int, input().split())

l = []

for i in range(n):
  l.append(int(input()))
t = sum(l)//k
h=1
while h<t:
  m = (h+t+1)//2
  s = 0
  for i in l:
    s+=i//m
  if s>=k:
    h=m
  else:
    t = m-1
print(h)