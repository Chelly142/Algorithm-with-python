n,k = map(int,input().split())

for i in range(k-1):
    if n<=k-i:
      print(0)
      break
    b=1
    while True:
      if b*2>n:
        break
      b= b*2
    n-=b
else:
  a=1
  while a<n:
    a=a*2
  print(a-n)