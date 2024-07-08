import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
r = list(range(1,n+1))
def back(combi,d):
    if d==m:
        print(*combi)

    else:
        for i in r:
            if i not in combi:
                next_combi = combi[:]
                next_combi.append(i)
                back(next_combi, d+1)
back([],0)