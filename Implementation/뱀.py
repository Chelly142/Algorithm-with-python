import heapq

n = 10
k=4
apple = [(0,1),(0,2),(0,3),(0,4)]
l = 4
flow = [(8,'D'),(10,'D'),(11,'D'),(13,'L')]
def flow_change():
  return True
def tail_cut():
  return True
def front():
  return True
second = 0
d = [(1,0),(0,1),(-1,0),(0,-1)]
head_x=0
head_y=0
snake=[]
heapq.heappush(snake,(0,0))

next_flow = heapq.heappop(flow)
now_d = (0,1)
while True:
  second+=1
  
  head_x+=now_d[0]
  head_y+=now_d[1]
  if head_x==-1 or head_x==n or head_y==-1 or head_y==n or [head_x,head_y] in snake:
    break
  else:
    heapq.heappush(snake,(head_x,head_y))
  if next_flow[0] == second:
      if next_flow[1]=='L':
        now_d = d[(d.index(now_d)+1)%4]
      elif next_flow[1]=='D':
        now_d = d[(d.index(now_d)-1)%4]
      if flow:
        next_flow = heapq.heappop(flow)
  if (head_x,head_y) not in apple:
    heapq.heappop(snake)
  else:
    apple.remove((head_x,head_y))
  
print(second)
