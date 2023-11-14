#바텀업으로 조져봅시당
t = int(input())
c =[]
for i in range(t):
  c.append(int(input()))
tabu = [(1,0),(0,1)]
def sol(x):
  for i in range(2,x+1):
    tabu.append((tabu[i-1][0]+tabu[i-2][0], tabu[i-1][1]+tabu[i-2][1]))
sol(max(c))

for i in c:
  print(tabu[i][0],tabu[i][1])
