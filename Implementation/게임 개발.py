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
