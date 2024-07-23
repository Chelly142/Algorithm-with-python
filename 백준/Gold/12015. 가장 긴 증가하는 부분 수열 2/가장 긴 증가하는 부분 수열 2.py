import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int,input().split()))

dp = [0]
a = [0]
def binary_search(t,a):
    start =0
    end = len(a)-1
    while start<=end:
        mid = (start+end)//2
        if a[mid+1]>=t>a[mid]:
            return mid+1
        if t>a[mid+1]:
            start = mid+1
        else:
            end = mid-1

for i in range(0,n):
    t = s[i]
    if t>a[-1]:
        a.append(t)
        dp.append(dp[-1]+1)
    else:
        index = binary_search(t,a)
        a[index] = t
print(max(dp))