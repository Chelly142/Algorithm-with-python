import sys
input = sys.stdin.readline

n,s =map(int,input().split())
a = list(map(int,input().split()))

prefix_sum = [0]*(n+1)
for i in range(1,n+1):
    prefix_sum[i] = prefix_sum[i-1]+a[i-1]

left = 0
right = 1
answer = 10e9
while right<n+1:
    part_len, part_sum = right-left,prefix_sum[right]-prefix_sum[left]
    if right==left:
        right+=1
        continue
    if part_sum>=s:
        answer = min(answer,part_len)
    if part_sum<=s:
        right+=1
    if part_sum>=s:
        left+=1
if answer == 10e9: print(0)
else: print(answer)
