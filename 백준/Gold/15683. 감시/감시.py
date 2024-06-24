#12:40 start
# cctv는 cctv 통과 가능 벽 통과 불가능
#사무실의 크기와 상태, 그리고 CCTV의 정보가 주어졌을 때
#CCTV의 방향을 적절히 정해서, 사각 지대의 최소 크기를 구하는 프로그램을 작성

n, m = map(int,input().split())
g = []
for i in range(n):
  g.append(list(map(int,input().split()))) 

#각 cctv별 시야 범위의 경우를 가지고있는 리스트

cases = []
# n, m = 6,6
# g = [[0,0,0,0,0,0],[0,2,0,0,0,0],[0,0,0,0,6,0],[0,6,0,0,2,0],[0,0,0,0,0,0],[0,0,0,0,0,5]]
# 출력 답 15

#각 cctv 종류 별로 돌렸을 때의 커버 범위를 반환하는 함수 작성
#근데 경우의 수가 굉장히 많아 질 것 같은 불안감
# + 4가지 경우를 어떤식으로 반환할지에 대한 불안감

def type1(graph, x, y):
  d1, d2, d3, d4 = [],[],[],[]
  for i in range(x,n):
    if graph[i][y]==6:
      break
    elif graph[i][y] == 0:
      d1.append((i,y))
  for i in range(x,-1,-1):
    if graph[i][y]==6:
      break
    elif graph[i][y] == 0:
      d2.append((i,y))
  for i in range(y,m):
    if graph[x][i]==6:
      break
    elif graph[x][i] == 0:
      d3.append((x,i))
  for i in range(y,-1,-1):
    if graph[x][i]==6:
      break
    elif graph[x][i] == 0:
      d4.append((x,i))
  cases.append([d1,d2,d3,d4])

def type2(graph, x, y):
  d1, d2 = [],[]
  for i in range(x,n):
    if graph[i][y]==6:
      break
    elif graph[i][y] == 0:
      d1.append((i,y))
  for i in range(x,-1,-1):
    if graph[i][y]==6:
      break
    elif graph[i][y] == 0:
      d1.append((i,y))
  for i in range(y,m):
    if graph[x][i]==6:
      break
    elif graph[x][i] == 0:
      d2.append((x,i))
  for i in range(y,-1,-1):
    if graph[x][i]==6:
      break
    elif graph[x][i] == 0:
      d2.append((x,i))
  cases.append([d1,d2])

def type3(graph, x, y):
  d1, d2, d3, d4 = [],[],[],[]
  for i in range(x,n): #아래
    if graph[i][y]==6:
      break
    elif graph[i][y] == 0:
      d1.append((i,y))
      d2.append((i,y))
  for i in range(x,-1,-1):
    if graph[i][y]==6:
      break
    elif graph[i ][y] == 0:
      d3.append((i,y))
      d4.append((i,y))
  for i in range(y,m): # 오른쪽
    if graph[x][i]==6:
      break
    elif graph[x][i] == 0:
      d1.append((x,i))
      d4.append((x,i))
  for i in range(y,-1,-1): # 왼쪽
    if graph[x][i]==6:
      break
    elif graph[x][i] == 0:
      d2.append((x,i))
      d3.append((x,i))
  cases.append([d1,d2,d3,d4])
#1:14 ~ 1:21 휴식
def type4(graph, x, y):
  d1, d2, d3, d4 = [],[],[],[]
  for i in range(x,n): #아래
    if graph[i][y]==6:
      break
    elif graph[i][y] == 0:
      d2.append((i,y))
      d3.append((i,y))
      d4.append((i,y))
  for i in range(x,-1,-1):
    if graph[i][y]==6:
      break
    elif graph[i][y] == 0:
      d1.append((i,y))
      d2.append((i,y))
      d4.append((i,y))
  for i in range(y,m): # 오른쪽
    if graph[x][i]==6:
      break
    elif graph[x][i] == 0:
      d1.append((x,i))
      d2.append((x,i))
      d3.append((x,i))
  for i in range(y,-1,-1): # 왼쪽
    if graph[x][i]==6:
      break
    elif graph[x][i] == 0:
      d1.append((x,i))
      d3.append((x,i))
      d4.append((x,i))
  cases.append([d1,d2,d3,d4])
def type5(graph, x, y):
  d1 = []
  for i in range(x,n): #아래
    if graph[i][y]==6:
      break
    elif graph[i][y] == 0:
      d1.append((i,y))
  for i in range(x,-1,-1):
    if graph[i][y]==6:
      break
    elif graph[i][y] == 0:
      d1.append((i,y))
  for i in range(y,m): # 오른쪽
    if graph[x][i]==6:
      break
    elif graph[x][i] == 0:
      d1.append((x,i))
  for i in range(y,-1,-1): # 왼쪽
    if graph[x][i]==6:
      break
    elif graph[x][i] == 0:
      d1.append((x,i))
  cases.append([d1])

obj = 0
for dx in range(n):
  for dy in range(m):
    if g[dx][dy] ==1:
      type1(g,dx,dy)
    if g[dx][dy] ==2:
      type2(g,dx,dy)
    if g[dx][dy] ==3:
      type3(g,dx,dy)
    if g[dx][dy] ==4:
      type4(g,dx,dy)
    if g[dx][dy] ==5:
      type5(g,dx,dy)
    if g[dx][dy] >0:
      obj+=1
# 전체 경우의 수? dfs, bfs? 조합?

# 막혀 버렸네...
answer = 0
def dfs(s, level=0, visited=[]):
  global answer
  for p in s:
    if p not in visited:
      visited.append(p)
  level+=1
  if level>=len(cases):
    answer = max(len(visited), answer)
    return answer
  for c in cases[level]:
    a = visited[:]
    dfs(c, level, a)
if len(cases)!=0:
  for i in cases[0]:
    dfs(i,0,[])
print(n*m-obj-answer)
  
      