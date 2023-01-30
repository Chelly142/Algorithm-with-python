from collections import deque
import copy
n =5
g = [(),(2,3,4),(),(4,5),(),()]
de = [0,0,1,1,2,1]
time =[0,10,10,4,4,3]
result =[0,10,10,4,4,3]
q = deque()
for i in range(1,n+1):
  if de[i] == 0:
    q.append(i)

while q:
  now = q.popleft()
  for i in g[now]:
    result[i] = max(result[i],time[i]+result[now])
    de[i]-=1
    if de[i] ==0:
      q.append(i)
print(result)

'''
사실 result 값을 처리해줄 때 max를 쓰는게 맞나 싶다.어떤 노드를 참조 할 때 경로가 두가지 있을 경우
예를 들어 1,2를 듣고 4를 들어하는 경우와 1,3을 듣고 4를 듣는경우 2가지가 존재 하면 저 알고리즘이 맞나?
틀리다고 생각 된다. 2와 3이 둘다 큐에 추가 되고 2가 pop 되었을 때 max 비교 때는 맞게 들어가겠지만 3이 pop 되면 min으로 바꾸어 주어야하기때문에 조건문 하나가 추가 되어야한다.
ex)
if result[i] == time[i]:
  result[i] = max(result[i],time[i]+result[now])
else:
  result[i] = min(result[i],time[i]+result[now])
'''
