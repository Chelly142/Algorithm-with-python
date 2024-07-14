import sys
import copy
from collections import deque
input = sys.stdin.readline
#13:54

n, k = map(int,input().split())

p = list(str(n))
p.sort(reverse=True)

def switch(number):
    str_n = list(str(number))
    a = []
    if len(str_n)==1:
        return -1
    if str_n == p:
        for i in range(1,len(p)):
            if p[i]==p[i-1]:
                return [int(''.join(str_n))]
        t = str_n[-1]
        str_n[-1] = str_n[-2]
        str_n[-2] = t
        if str_n[0] == '0':
            return -1
        return [int(''.join(str_n))]
    for i in range(len(str_n)):
        if str_n[i]==p[i]:
            continue
        else:
            cases =[]
            for j in range(i+1,len(str_n)):
                if str_n[j]==p[i]:
                    cases.append(j)
            for j in cases:
                str_n_copy = copy.deepcopy(str_n)
                t = str_n_copy[j]
                str_n_copy[j] = str_n_copy[i]
                str_n_copy[i] = t
                a.append(int(''.join(str_n_copy)))
            break
    if str_n[0] =='0':
        return -1
    return a

q = deque([(n,0)])
answer = []

while q:
    now,d = q.popleft()
    if d == k:
        answer.append(now)
    else:
        nexts = switch(now)
        if nexts != -1:
            for next in nexts:
                q.append((next,d+1))
if answer:
    print(max(answer))
else:
    print(-1)
#14:46 6% 틀림