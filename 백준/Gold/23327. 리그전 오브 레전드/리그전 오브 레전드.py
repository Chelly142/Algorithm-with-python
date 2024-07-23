import sys
input = sys.stdin.readline

#12:40 
n, q = map(int, input().split())
team_like_list = list(map(int,input().split()))
prefix_sum = [0]*(n+1)
total = [0]*(n+1)
for i in range(1,n+1):
    prefix_sum[i]=prefix_sum[i-1]+team_like_list[i-1]
    total[i]=total[i-1]+prefix_sum[i-1]*team_like_list[i-1]

def calc_fun(l,r):
    fun = 0
    for i in range(l,r+1):
            fun += team_like_list[i-1]*(prefix_sum[r]-prefix_sum[i])
    return fun

answer = []
for i in range(q):
    l,r = map(int,input().split())
    result = 0
    if l==1:
        result = total[r]
    else:
         result = total[r]-total[l-1]-(prefix_sum[r]-prefix_sum[l-1])*prefix_sum[l-1]
    answer.append(result)
print(*answer,sep="\n")
