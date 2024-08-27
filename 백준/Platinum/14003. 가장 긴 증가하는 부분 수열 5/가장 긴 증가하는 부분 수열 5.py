from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int,input().split()))

l = [0]*(n)
l[0]=1
dp = [A[0]]

def binary_search(x):
    start, end= 0, len(dp)-1
    while start<=end:
        mid = (start+end)//2
        if dp[mid]>=x:
            end = mid-1
        else:
            start = mid+1
    return start

for i in range(1,n):
    if dp[-1]<A[i]:
        dp.append(A[i])
        l[i] = len(dp)
    else:
        idx = binary_search(A[i])
        dp[idx] = A[i]
        l[i]=idx+1
print(len(dp))

t= max(l)
k = l.index(t)
answer = []
while k>=0 and t>0:
    if l[k]==t:
        answer.append(A[k])
        t-=1
    k-=1
print(*sorted(answer))