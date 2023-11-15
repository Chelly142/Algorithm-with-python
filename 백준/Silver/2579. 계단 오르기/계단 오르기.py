# n 번째 칸에 도착하는 방법
# 3칸전 밟고 1칸전 밟고 오는 경우
# 2칸전 밟고 오는 경우
# case 1 : memo[n] = memo[n-3]+s[n-1]+s[n]
# case 2 : memo[n] = memo[n-2]+s[n]
# 두 경우중 큰 경우를 채택
# i번째 칸에 오면 
# 메모제이션을 하지않으면 시간초과
n = int(input())
s=[0]

for i in range(n):
  s.append(int(input()))
s.append(0)
memo = [0]*(n+2)
memo[1] = s[1]
memo[2] = s[1]+s[2]

def step(x):
  if x==0:
    return 0
  if x==1:
    return memo[1]
  if x==2:
    return memo[2]
  if memo[x]==0:
    memo[x] = max( step(x-3)+s[x-1]+s[x], step(x-2)+s[x] )
  return memo[x]
   
print(step(n))

