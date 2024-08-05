import sys
sys.setrecursionlimit(111111)
input = sys.stdin.readline

#15:39
n = int(input())
A = list(map(int, input().split()))

stack  =[]

NGE_list = [-1]*n

for i in range(0,n):
      while stack and A[stack[-1]]<A[i]:
            NGE_list[stack.pop()] = A[i]
      stack.append(i)
print(*NGE_list)