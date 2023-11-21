
n = int(input())
l = list(map(int,input().split()))

# memo = []
# for i in range(n):
#   memo.append(l[i])
# #i번째가 들어가는 경우 나머지들과의 관계 비교
# for i in range(n):
#   s=0
#   for j in range(i+1,n):
#     s += l[j] #이 놈을 재활용 해야 할 듯
#     memo[j] = max(memo[i]+s,memo[j])
# print(max(memo))
# 시간 초과

#고려하는 숫자의 개수별로 루프를 돌려보자
# memo = []
# for i in range(n):
#   memo.append(l[i])
# answer = -2**31
# for i in range(1,n+1):
#   for j in range(0,n-i):
#     memo[j] = memo[j]+l[j+i]
#   answer = max(answer, max(memo))
# print(answer)
# 시간 초과

#야발 탑다운 재귀로 가보자
#여전히 개수 고려로
#아니다 걍 첫번째 고려를 다듬어 보자
#첫번쨰 원소를 넣는다 가정했을떄의
#모든 경우의 수를 구하고
#다음 루프에서는 원래 수를 빼면서 계산
# memo = []
# s=0
# for i in range(0,n):
#   s += l[i]
#   memo.append(s)
# answer = max(memo)
# for i in range(1,n):
# 시간초과
# n제곱에서 벗어나야한다

#for문을 한번만 돌면서 숫자 하나씩 추가하면서
#더 큰 값이 나오면 폐기 및 채택하는 방식
#다음수가 음수인지 양수인지 경우 나눔
#음수가 나올때 마다 기록
left = 0
memo = [0]*n
for i in range(0,n):
  if l[i]<0:
    if left+l[i]<0: #음수 기준 왼쪽 최대와 음수 합이 음수이면 폐기
      left = 0
      memo[i] = l[i]
    else:
      left+=l[i]
  else:
    left+=l[i]
    memo[i] = left


print(max(memo))