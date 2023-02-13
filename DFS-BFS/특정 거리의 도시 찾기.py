from collections import deque
n,m,k,x = map(int,input().split())#입력부
graph = []#도로 그래프
for i in range(m):#도로 입력 반복문
    graph.append(list(map(int,input().split())))
min_d = [300000]*(n+1)#최단거리 저장 인덱스가 그 방향까지의 최단거리
visit =[0]*(n+1)#방문 표시 인덱스가 그 도시 번호
min_d[x]=0#시작 점은 거리가 0
visit[x]=1
q = deque([x])#BFS를 위한 큐 초기값으로 시작 도시 넣음
while q:# 큐가 빌때까지 반복 = 다 방문했거나 노드가 남았으면 갈방법이 없음
    now = q.popleft()#현재 노드를 큐에서 빼옴
    for i in graph:#도로 그래프에 대해
        if i[0] == now and not visit[i[1]]:#현재 노드와 시작노드가 같고 도착노드에 방문하지 않았을 경우
            q.append(i[1])#큐에 도착 노드 추가
            min_d[i[1]] = min_d[i[0]]+1#최소 거리 경신
            visit[i[1]] = 1#방문표시
c = min_d.count(k)#최소거리가 k인 개수 
if c:#c가 0이 아닐 경우
    for i,v in enumerate(min_d):
        if v == k:
            print(i)
else:#c가 0
    print(-1)
m = 4
n=4
k=1
x=1
ENF=10e9
r = [(1,2),(1,3),(2,3),(2,4)]
stack = []
d = [ENF]*(m+1)
d[x] = 0
for i in r:
  if i[0] == x:
    stack.append(i)
while stack:
  road = stack.pop()
  for i in r:
    if road[1] == i[0]:
      stack.append(i)
  d[road[1]] = min(d[road[1]],d[road[0]]+1)

for i,v in enumerate(d):
  if v==k:
    print(i)
if k not in d:
  print(-1)
