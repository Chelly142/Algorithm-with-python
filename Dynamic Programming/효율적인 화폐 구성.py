n, m = map(int,input().split())
l=[]
d =[10001]*(m+1)
for i in range(n):
    l.append(int(input()))

d[0] = 0
for i in range(n):
    for j in range(l[i],m+1):
        d[j] =min(d[j],d[j-l[i]]+1)
if d[m]!= 10001:
    print(d[m])
else:
    print(-1)

#진짜 줜나게 어렵고 다보고 배낀 수준 무줘건 다시 작성해볼것!
n,m =3,40
c =[3,5,7]
d = [10001]*(m+1)

#a(n) = min(a(n-2),a(n-3)) + 1 
for i in range(min(c),m+1):
  array =[]
  if i in c:
    d[i] = 1
    continue
  else:
    for j in c:
      if i>=j:
        array.append(d[i-j])

  d[i] = min(array)+1


if d[m]>10000:
  print(-1)
else:
  print(d[m])
#성장했구나 세현아!
