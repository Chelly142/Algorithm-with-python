import sys
from collections import deque
input = sys.stdin.readline
n= int(input())
answer = []
def hanoi(x,f,t,a):
    if x==1:
        answer.append((f,t))
        return 1
    hanoi(x-1,f,a,t)
    answer.append((f,t))
    hanoi(x-1,a,t,f)
hanoi(n,1,3,2)
print(len(answer))
for a,b in answer:
    print(a,b)