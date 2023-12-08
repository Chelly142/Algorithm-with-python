#15:05
#이런 것도 dp긴 하지
#테스트 케이스 할때마다 메모
#누적합은 뭐고 첨보네
import sys 
input = sys.stdin.readline
n,m = map(int,input().split())
g = []
for i in range(n):
  g.append(list(map(int,input().split())))
tabu = [[0]*(n+1) for x in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
      tabu[i][j] = g[i-1][j-1]+tabu[i-1][j]+tabu[i][j-1]-tabu[i-1][j-1]

answer = []
for i in range(m):
  x1,y1,x2,y2 = map(int,input().split())
  s = tabu[x2][y2]-tabu[x1-1][y2]-tabu[x2][y1-1]+tabu[x1-1][y1-1]
  answer.append(s)
for i in answer:
  print(i)
  
  