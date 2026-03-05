import heapq

n= int(input())
tasks = []
for _ in range(n):
    a, b = map(int, input().split())
    tasks.append((a, b))

tasks.sort(key=lambda x: x[0])

pq = []

for deadline, reward in tasks:
  heapq.heappush(pq,  reward)
  if(len(pq) > deadline):
    heapq.heappop(pq)

print(sum(pq))