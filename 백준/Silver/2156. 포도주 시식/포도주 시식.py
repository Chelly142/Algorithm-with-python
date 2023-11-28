#n번째 넣었을때 최대는
#max(g(n)+g(n-1),g(n)+g(n-2))
#틀릴듯
# n = int(input())
# g =[0]
# for i in range(n):
#   g.append(int(input()))
# memo = [0]*(n+1)
# memo[1] = g[1]
# memo[2] = g[1]+g[2]

# for i in range(3,n+1): #번째
#   memo[i] = memo[i-3]+max(g[i]+g[i-1], g[i]+g[i-2])
# print(memo)

#각 메모에 바로전거랑 연속되어 포함되는 경우랑 단일로 포함되는 경우
#두가지 경우를 메모해야 3번 연속되는 경우를 방지 할 수 있음
n = int(input())
g =[0]
for i in range(n):
  g.append(int(input()))
memo = [[0,0]]
if n>2:
  memo.append([g[1],g[1]]) 
  memo.append([g[2],g[1]+g[2]])
  answer =g[1]+g[2]
else:
  answer = sum(g)
for i in range(3,n+1): #번째
  l = [0,0]
  l[0] = max(max(memo[i-2])+g[i],memo[i-1][1])
  l[1] = max(memo[i-1][0]+g[i],memo[i-1][1])
  
  memo.append(l)
  answer = max(answer,l[0],l[1])
print(answer)
