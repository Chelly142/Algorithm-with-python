n = input()
k=0
a=0
b=0
for i in n:
    if k<len(n)/2 :
        a+=int(i)
    else:
        b+=int(i)
    k+=1
if b == a:
    print("LUCKY")
else:
    print("READY")

n=input()
l = len(n)
left, right =0,0
for i in n[:int(l/2)]:
  left+=int(i)
for i in n[int(l/2):]:
  right+=int(i)
if (left-right):
  print("READY")
else:
  print("LUCKY")
