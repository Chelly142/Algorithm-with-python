def sol(n, a):
  p = a[-1] #팔면 최대 이득 날
  s = 0 #그 날 팔 매물 수
  answer = 0
  for i in range(n-1,-1,-1):
    if a[i] < p:
      answer+=(p-a[i])
    else:
      p = a[i]
  return answer

t = int(input())
for i in range(t):
  n = int(input())
  a = list(map(int, input().split()))
  print(sol(n,a))
