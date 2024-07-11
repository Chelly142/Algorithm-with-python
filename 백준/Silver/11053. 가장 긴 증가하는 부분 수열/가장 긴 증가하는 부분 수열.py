import sys
input = sys.stdin.readline


n = int(input())
l = tuple(map(int,input().split()))

dp = [0]
a = [0]

# 3:26
# 3:31 LIS 작성

def binary_search(target, lst):
    start, end = 0, len(lst)-1
    while start<end:
        mid = (start+end)//2
        if lst[mid]<target<=lst[mid+1]:
            return mid+1
        elif target>lst[mid+1]:
            start = mid+1
        else:
            end = mid

for i in range(1,n+1):
    t = l[i-1]
    if t>a[-1]:
        dp.append(dp[-1]+1)
        a.append(t)
    else:
        idx = binary_search(t,a)
        a[idx] = t
print(max(dp))
