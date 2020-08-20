import itertools

n = int(input())#수의 개수
a = list(map(int,input().split())) #수 리스트 순서 불변
calc = list(map(int,input().split()))# 연산자 리스트 개수 리스
c=[]
for i,v in enumerate(calc):
    c+=[i]*v
p = list(itertools.permutations(c,len(c)))
max_s = -1.0e10
min_s = 1.0e10
for k in p:
    s=a[0]
    for i in range(0,len(a)-1):
        if k[i]==0:
            s+=a[i+1]
        if k[i]==1:
            s-=a[i+1]
        if k[i]==2:
            s*=a[i+1]
        if k[i]==3:
            if s<0 and a[i+1]>0:
                s= s//a[i+1]+1
            else:
                s//=a[i+1]
    max_s = max(max_s,s)
    min_s = min(min_s,s)
print(max_s)
print(min_s)
