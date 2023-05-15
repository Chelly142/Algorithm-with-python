n = int(input())
l = int(input())
networks = []
for i in range(l):
  networks.append(list(map(int,input().split())))

net_v = [0]*len(networks)
sol = [1]
def dfs(start):
  for i,v in enumerate(networks):
    if net_v[i]==0 and start in v:
      net_v[i] = 1
      if v[0] == start:
        a= v[1]
      else:
        a=v[0]
      if a not in sol:
        sol.append(a)
        dfs(a)

dfs(1)
print(len(sol)-1)