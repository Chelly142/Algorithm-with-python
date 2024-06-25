#1:02 시작
t = []
for _ in range(4):
  t.append(input())
k = int(input())

# index 0 톱니바퀴 번호
# index 1 돌리는 방향 1->시계 -1->반시계
step = []
for _ in range(k):
  step.append(list(map(int,input().split()))) 

def turn(topni, direc):
  if direc ==1:
    return topni[-1]+topni[:7]
  if direc ==-1:
    return topni[1:]+topni[0]

def find_turn_num():
  a =[]
  for i in range(3):
    if t[i][2]==t[i+1][6]:
      a.append(False)
    else:
      a.append(True)
  return a
def turn_all(t_num, direc): #-1 해서 t_num 줄것
  left = t_num
  l_d = direc
  right = t_num
  r_d = direc

  a = find_turn_num()
  t[t_num] = turn(t[t_num],direc)
  while left-1>=0 and a[left-1]:
    left -= 1
    l_d *= -1
    t[left] = turn(t[left], l_d)
  while right+1<4 and a[right]:
    right += 1
    r_d *= -1
    t[right] =turn(t[right], r_d)
  return t
for s in step:
  turn_all(s[0]-1,s[1])
answer = 0

for i in range(4):
  answer+=int(t[i][0])*(2**i)
print(answer)