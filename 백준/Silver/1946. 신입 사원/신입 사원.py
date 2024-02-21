def solution(n, result):
  result.sort()
  dropout = 0
  k = result[0][1]
  for i in range(1,n):
    if k<result[i][1]:
      dropout+=1
    k = min(k,result[i][1])
  return n-dropout

t= int(input())
answer = []
for i in range(t):
  n = int(input())
  result = []
  for j in range(n):
    result.append(tuple(map(int,input().split())))
  answer.append(solution(n,result))
for k in answer:
  print(k)