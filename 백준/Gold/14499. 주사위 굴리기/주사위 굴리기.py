#2:39
n,m,x,y,k = map(int,input().split())
g =[]
for i in range(n):
  g.append(list(map(int,input().split())))
orders = list(map(int,input().split()))
# n,m,x,y,k = [4,2,0,0,8]
# g=[[0,2],[3,4],[5,6],[7,8]]
# orders = [4,4,4,1,3,3,3,2]

dice = [0,0,0,0,0,0]
def write(x,y):
  if g[x][y]==0:
    g[x][y] = dice[5]
  else:
    dice[5] = g[x][y]
    g[x][y]=0 

def roll(direc):
  global y
  global x
  global dice
  if direc == 1 and y+1<m:
    y+=1
    d1,d2,d3,d4,d5,d6 = dice
    dice = [d4,d2,d1,d6,d5,d3]
    write(x,y)
    print(dice[0])
  if direc == 2 and y-1>=0:
    y-=1
    d1,d2,d3,d4,d5,d6 = dice
    dice = [d3,d2,d6,d1,d5,d4]
    write(x,y)
    print(dice[0])
  if direc == 3 and x-1>=0:
    x-=1
    d1,d2,d3,d4,d5,d6 = dice
    dice = [d5,d1,d3,d4,d6,d2]
    write(x,y)
    print(dice[0])
  if direc == 4 and x+1<n:
    x+=1
    d1,d2,d3,d4,d5,d6 = dice
    dice = [d2,d6,d3,d4,d1,d5]
    write(x,y)
    print(dice[0])
  
for o in orders:
  roll(o)