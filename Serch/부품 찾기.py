def bs(array,target,start,end):
    if start>end:
        return "no"
    mid = (start+end)//2
    if array[mid] == target:
        return "yes"
    elif array[mid]>target:
        end = mid-1
    else:
        start = mid+1
    return bs(array,target,start,end)


n = int(input())
a = list(map(int,input().split()))
a.sort()
m = int(input())
b = list(map(int,input().split()))
for i in b:
    print(bs(a,i,0,n-1),end =' ')
#set 과 계수정렬로도 풀수있음
