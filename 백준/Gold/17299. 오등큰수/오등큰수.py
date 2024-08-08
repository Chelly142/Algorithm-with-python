import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
num_cnt={}
for i in range(n):
    if A[i] in num_cnt:
       num_cnt[A[i]]+=1
    else:
        num_cnt[A[i]] = 0

stack = [0]
answer = [-1]*n

for i in range(1,n):
    while stack and num_cnt[A[stack[-1]]]<num_cnt[A[i]]:
        answer[stack.pop()] = A[i]
    stack.append(i)
print(*answer)
      