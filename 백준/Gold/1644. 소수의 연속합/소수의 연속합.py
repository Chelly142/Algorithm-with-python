import sys
input = sys.stdin.readline

n = int(input())
eratos = [True]*(n+1)
prime_nums = []

for i in range(2,n+1):
    if eratos[i]:
        prime_nums.append(i)
        for j in range(i,n+1-i,i):
            eratos[i+j] = False

prefix_sum = [0]*(len(prime_nums)+1)

for i in range(1,len(prime_nums)+1):
    prefix_sum[i] = prefix_sum[i-1]+prime_nums[i-1]

left = 0
right = 1
answer = 0
while right<len(prefix_sum):
    part_sum = prefix_sum[right]-prefix_sum[left]
    if part_sum==n:
        answer+=1
    if part_sum>=n:
        left+=1
    if part_sum<=n:
        right+=1
print(answer)
    

