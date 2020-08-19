n,k = map(int,input().split())
graph =[]
for i in range(n):
    graph.append(list(map(int,input().split())))
s,x,y = map(int,input().split())

a =[]
for i in range(n):
        for j in range(n):
            if graph[i][j]:
                a.append([graph[i][j],i,j])#[우선순위 ,x, y]
a.sort()

def second_work(c,m):
    k=[]
    for i in m:
        if n>i[1]>-1 and n>i[2]>-1:
            k.append(i)
    m=k
    #print(m)    
    if c==s:
        print(graph[x-1][y-1])
        return True
    for i in m:
        if graph[i[1]][i[2]] == 0 or graph[i[1]][i[2]] == i[0]:
            graph[i[1]][i[2]] = i[0]
    a=[]
    flag = 1
    for i in range(n):
        for j in range(n):
            if graph[i][j]:
                a.append([graph[i][j],i+1,j])
                a.append([graph[i][j],i-1,j])
                a.append([graph[i][j],i,j+1])
                a.append([graph[i][j],i,j-1])
            else:
                flag = 0
    if flag == 1:
        print(graph[x-1][y-1])
        return True
    a.sort()#정렬
 
    second_work(c+1,a)
    return True
second_work(-1,a)
