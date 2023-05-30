#10:14
n = int(input())
g = [list(map(int,input().split())) for _ in range(n)]




for x in range(n):
  for y in range(n):
      for z in range(n):
        if g[y][z] == 0:
          if g[y][x] == 1 and g[x][z] == 1:
            g[y][z] = 1

for i in g:
  print(*i)
