n,l,r =map(int,input().split())
m = []
visit = []#방문한 좌표들 리스트
now_g =[]
#이번 턴 그룹별 모음
turn_g =[]
for i in range(n):
    m.append(list(map(int,input().split())))

def dfs(x,y):
    #현재 좌표에 방문한 경우
    if [x,y] in visit:
        return False
    #이번 턴 방문한 좌표
    visit.append([x,y])
    #현재 그룹에 대한 좌표들
    now_g.append([x,y])
    if  x+1<n and l<= max(m[x+1][y],m[x][y]) - min(m[x+1][y],m[x][y])<=r:#조건에맞으며 범위에 벗어나는가?
        dfs(x+1,y)
    if  x-1>-1 and l<= max(m[x-1][y],m[x][y]) - min(m[x-1][y],m[x][y])<=r:
        dfs(x-1,y)
    if  y+1<n and l<= max(m[x][y+1],m[x][y]) - min(m[x][y+1],m[x][y])<=r:
        dfs(x,y+1)
    if  y-1>-1 and l<= max(m[x][y-1],m[x][y]) - min(m[x][y-1],m[x][y])<=r:
        dfs(x,y-1)
    return True    

flag =True
turn=0
while flag:
    visit=[]
    turn_g=[]
    flag=False
    for i in range(n):
        for j in range(n):
            now_g=[]
            dfs(i,j)
            if len(now_g)>1:
                flag =True
                turn_g.append(now_g)            
    for v in turn_g:
        s=0
        for k in v:
            s+=m[k[0]][k[1]]
        for k in v :
            if len(v)>1:
                m[k[0]][k[1]] = s//len(v)
    if flag:
        turn+=1
print(turn)
