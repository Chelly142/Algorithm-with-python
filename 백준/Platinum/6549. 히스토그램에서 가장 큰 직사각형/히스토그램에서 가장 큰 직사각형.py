import sys
import copy
input = sys.stdin.readline




def dnc(start, end, h):
    if start>=end:
        return 0
    if end-start==1:
        return h[start]
    
    mid = (start+end)//2
    answer = max(dnc(start,mid,h),dnc(mid,end,h))
    l=mid
    r=mid
    now_h=h[mid]
    while r-l+1<end-start:
        p = 0
        q = 0
        if l>start:
            p = min(now_h,h[l-1])
        else:
            p = -1
        if r<end-1:
            q = min(now_h,h[r+1])
        else:
            q = -1
        if p>=q:
            now_h=p
            l-=1
        else:
            now_h=q
            r+=1
        answer = max(answer,(r-l+1)*now_h)
        
    return answer

h = 1
answer =[]
while h!=[0]:
    h = list(map(int,input().split()))
    if h==[0]:
        break
    answer.append(dnc(1,len(h),h))
print(*answer,sep="\n")