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
