
import sys
sys.setrecursionlimit(1000000)
def solution(n):
    answer = []
    tr = []

    for i in range(n):
        tr.append([0]*(i+1))
    
    def snail(h, sn ,d,sx,sy):
        if h==1:
            tr[sx][sy]=sn
        elif d==1:
            for i in range(h):
                tr[sx+i][sy] = sn
                sn+=1
            snail(h-1,sn,2,sx+h-1,sy+1)
        elif d==2:
            for i in range(h):
                tr[sx][sy+i] = sn
                sn+=1
            snail(h-1,sn,3,sx-1,sy+h-2)
        else:
            for i in range(h):
                tr[sx-i][sy-i] = sn
                sn+=1
            snail(h-1,sn,1,sx-h+2,sy-h+1)
    snail(n,1,1,0,0)
    for i in tr:
        for j in i:
            answer.append(j)
    return answer