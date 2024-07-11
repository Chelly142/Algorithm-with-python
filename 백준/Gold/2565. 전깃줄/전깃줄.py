import sys
input = sys.stdin.readline

# a = 1,2,3,4,6,7,9,10
# b = 8,2,9,1,4,6,7,10
# answer = n - b의 LIS의 길이
# b의 LIS의 길이를 구하자

n = int(input())
lines = [tuple(map(int,input().split())) for _ in range(n)]
lines.sort()
b = [0]+[i[1] for i in lines]


dp = [0]
a = [0]
def binary_search(target,l):
    start,end = 0,len(l)-1
    while start < end:
        mid = (start+end)//2
        if l[mid-1]<target<=l[mid]:
            return mid
        elif l[mid]<target:
            start = mid+1
        else:
            end = mid-1
    return start
for i in range(1,n+1):
    if b[i]>a[-1]:
        dp.append(dp[-1]+1) 
        a.append(b[i])
    else:
        idx = binary_search(b[i],a)
        a[idx] = b[i]

print(n-max(dp))

    