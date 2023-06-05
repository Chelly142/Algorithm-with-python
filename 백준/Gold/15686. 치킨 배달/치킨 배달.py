from itertools import combinations
n,m = map(int,input().split())
house = []
chicken = []
for i in range(n):
  a = list(map(int,input().split()))
  for j in range(n):
    if a[j] == 1:
      house.append((i,j))
    if a[j] == 2:
      chicken.append((i,j))
chi_d =[]

for i in chicken:
  temp =[]
  for j in house:
    temp.append(abs(i[0]-j[0])+abs(i[1]-j[1]))
  chi_d.append(temp)

answer =[]
for i in combinations(range(len(chicken)),m):
  t=0
  for j in range(len(house)):
    a=2000000
    for k in i:
      a = min(a,chi_d[k][j])
    t+=a
  answer.append(t)
print(min(answer))
