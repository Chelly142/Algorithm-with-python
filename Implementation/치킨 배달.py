from itertools import combinations, permutations

n = 5
m = 1
city = [[1,2,0,2,1],[1,2,0,2,1],[1,2,0,2,1],[1,2,0,2,1],[1,2,0,2,1]]
home = []
chicken =[]
chicken_d =[]
#집당 모든 치킨 거리 구하기
def find_chicken(x,y):
  return True

#치킨 집 좌표랑 집 좌표 각각ㄱ 리스트에 저장
for x in range(n):
  for y in range(n):
    if city[x][y] == 2:
      chicken.append((x,y))
    if city[x][y] == 1:
      home.append((x,y))
#집기준으로 모든 치킨집 치킨 거리 저장
for h in home:
  l = []
  for c in chicken:
    l.append(abs(h[0]-c[0])+abs(h[1]-c[1]))
  chicken_d.append(l)

#폐점 경우의 수당 min 합을 내 그중에서 도 최솟값
nums = []
for i in range(len(chicken)):
  nums.append(i)
answer = 10000000
combi = list(combinations(nums, m))

for c in combi:
  s = 0
  for cd in chicken_d:
    h_min = 13
    for i,v in enumerate(cd):
      if i in c:
        h_min = min(h_min,v)
    s+=h_min
  answer = min(s,answer)
print(answer)
