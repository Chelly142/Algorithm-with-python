from collections import deque
import itertools
from copy import *
n = int(input())
m = []#지도 그래프
temp_m = []
t_position = []#선생님들의 위치정보
s_position = []#학생들의 위치 정보
x_position = []#빈공간
for i in range(n):
    k = list(input().split())
    m.append(k)
    for j,v in enumerate(k):
        if v == "T":
            t_position.append((i,j))
        elif v == "S":
            s_position.append((i,j))
        else:
            x_position.append((i,j))

w_position = list(itertools.combinations(x_position,3))
index =[-1,1]#선생님이 바라보는 방향
    
def find_student(wall_m):#주어진 지도 wall_m에 대해 선생님들의 학생 수색 함수
    for i in t_position:#각 선생님들의 첨 위치에 대해
        for j in index:#x축에 대해
            k = list(i)
            while -1<k[0]<n:#맵 밖으로 나옴
                if wall_m[k[0]][k[1]] == "O":#벽이라 이쪽방향 탐색 끝
                    break
                if wall_m[k[0]][k[1]] == "S": #학생 찾음
                    return True
                k[0] += j#보고있는 방향으로 한발자국 더나감
        for j in index:
            k=list(i)
            while -1<k[1]<n:
                if wall_m[k[0]][k[1]] == "O":
                    break
                if wall_m[k[0]][k[1]] == "S":
                    return True
                k[1] += j
    return False

flag = 0
for i in w_position:
    temp_m = deepcopy(m)
    for j in i:
        temp_m[j[0]][j[1]] = "O"
    if not find_student(temp_m):
        flag = 1
        break
if flag == 1:
    print("YES")
else:
    print("NO")
    
