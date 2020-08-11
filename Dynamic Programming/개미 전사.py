n = int(input())
k = list(map(int,input().split()))
d= [[k[0],0]]+[[0,0]]*(n-1)
for i in range(1,n):
    d[i] = [d[i-1][1]+k[i],d[i-1][0]]
print(max(d[n-1]))
# 풀긴 했지만 조금더 바텀업방식 익숙해질 필요가 있음
