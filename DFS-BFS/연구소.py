from itertools import combinations #기둥 3개 뽑기위해 조합사용
import copy

n,m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))

virus =[]
void = []

for i,k in enumerate(graph):
    for j,v in enumerate(k):
        if v==2:
            virus.append([i,j])
        if v==0:
            void.append([i,j])

def post_virus(ma,x,y):#now는 현재 좌표 바이러스 퍼뜨리는 dfs 재귀 함수임
    if x<0 or n <= x or m <= y or y<0: #지도를 벗어날경우
        return False
    if ma[x][y]==0:#방문가능일 경우 (0인 경우)
        ma[x][y] = 2
        post_virus(ma,x-1, y)
        post_virus(ma,x+1, y)
        post_virus(ma,x, y-1)
        post_virus(ma,x, y+1)
        return False
    return True # 방문하지 않을경우
result = -1
for i in combinations(void,3):#빈 공간 3개를 뽑아 기둥으로 만듦
    a = copy.deepcopy(graph)
    sum_safe = 0
    for j in i:
        a[j[0]][j[1]]=1
    for k in virus:
        a[k[0]][k[1]]=0
        post_virus(a,k[0],k[1])
    for c in a:
        sum_safe += c.count(0)
    result = max(result,sum_safe)
print(result)
