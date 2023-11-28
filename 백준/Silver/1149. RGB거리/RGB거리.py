# n번쨰 집에서 3가지 색 모두 배열에 저장하면서 가능한 n-1번호중
# 최소 + 현재 색갈 집 값
n = int(input())
g =[]
for i in range(n):
  g.append(list(map(int,input().split())))

memo =[g[0]]
for i in range(1,n):
  l=[0,0,0]
  l[0] = g[i][0]+min(memo[i-1][1],memo[i-1][2])
  l[1] = g[i][1]+min(memo[i-1][0],memo[i-1][2])
  l[2] = g[i][2]+min(memo[i-1][0],memo[i-1][1])
  memo.append(l)
print(min(memo[n-1]))