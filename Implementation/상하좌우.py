n = int(input())
plan_char  = input().split()
x = 1
y = 1
for c in plan_char:
  if c == 'R' and x!= n:
    x+=1
  if c == 'L' and x!= 1:
    x-=1
  if c == 'D' and y!= n:
    y+=1
  if c == 'U' and y!= 1:
    y-=1
  print(x,y)