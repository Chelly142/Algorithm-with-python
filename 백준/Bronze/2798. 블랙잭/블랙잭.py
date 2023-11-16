import itertools
n, m = map(int,input().split())
cards = list(map(int,input().split()))

answer = 0
combi = itertools.combinations(cards,3)
for i in combi:
  t = sum(i)
  if answer<t<m:
    answer = t
  if t == m:
    answer = t
    break
print(answer)
    