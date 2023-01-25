n, m = map(int, input().split())
a, b, d = map(int, input().split())
w=[]
k = [(0,-1),(1,0),(0,1),(-1,0)]
l =[(a,b)]
flag =1
for i in range(m):
    w.append(list(map(int,input().split())))

while flag:
    D = [(d+3)%4,(d+2)%4,(d+1)%4,d]
    for i in D:
        if i == d:
            a+=k[D[1]][0]
            b+=k[D[1]][1]
            if n>a>=0 and m>b>=0 and w[b][a] != 1:
                l.append((a,b))
            else:
                flag =0
        a += k[i][0]
        b += k[i][1]
        if n>a>=0 and m>b>=0 and w[b][a] != 1 and (a,b) not in l:
            l.append((a,b))
            d = i
            break
        else:
            a -= k[i][0]
            b -= k[i][1]
        
        
result = len(set(l))
print(result)

'''
2020 임세현 괴물 그 자체네 ㅋㅋ
x,y =map(int,input().split())
x1,y1,d =map(int,input().split())
check=[[0]*y for _ in range(x)]
array = []
for i in range(x):
  array.append(list(map(int,input().split())))
steps = [(-1,0),(0,1),(1,0),(0,-1)]
flag =True
cnt = 1
check[x1][y1] = 1
while flag:
  for i in range(1,5):
    new_x = x1+steps[d-i][0]
    new_y = y1+steps[d-i][1]
    flag = False
    if x>new_x>=0 and y>new_y>=0 and array[new_x][new_y] == 0 and check[new_x][new_y] == 0:
      x1 = new_x
      y1 = new_y
      check[new_x][new_y] = 1
      d = d-i
      cnt+=1
      if d < 0:
        d += 4
      flag = True      
      break
    
  if not flag:
    back_x = x1-steps[d][0]
    back_y = y1-steps[d][1]
    if x>back_x>=0 and y>back_y>=0 and array[back_x][back_y] == 0:
      x1 = back_x
      y1 = back_y
      flag = True
    else :
      flag = False
print(cnt)
'''