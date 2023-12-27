#어떤수를 포함하는 합이 가장 큰 수열은 단 하나이다
n = int(input())
a = list(map(int,input().split()))
answer =a[0]
dp = [[a[0],a[0]]]
for i in range(1,n):
  s=a[i]
  for j in dp:
    if j[0]<a[i]:
      s = max(s,j[1]+a[i])
  dp.append([a[i],s])
  answer = max(answer,s)
print(answer)