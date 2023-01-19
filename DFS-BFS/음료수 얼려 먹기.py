from collections import deque 


n, m = map(int,input().split())
l = []
visited =[]
for i in range(n):
    l.append(list(map(int,input())))
    visited.append([False]*m)
result =0

que = deque()
for i in range(n):
    for j in range(m):
        if l[i][j] == 0 and not visited[i][j]:
            visited[i][j] = True
            que.append([i,j])
            while que:
                v = que.popleft()
                
                if v[0]+1 < n and l[v[0]+1][v[1]] == 0 and not visited[v[0]+1][v[1]]:
                    que.append([v[0]+1,v[1]])
                    visited[v[0]+1][v[1]] = True
                    
                if v[0]-1 >= 0 and l[v[0]-1][v[1]] == 0 and not visited[v[0]-1][v[1]]:
                    que.append([v[0]-1,v[1]])
                    
                    visited[v[0]-1][v[1]] = True
                if v[1]+1 < m and l[v[0]][v[1]+1] == 0 and not visited[v[0]][v[1]+1]:
                    que.append([v[0],v[1]+1])
                    visited[v[0]][v[1]+1] = True
                
                if v[1]-1 >= 0 and l[v[0]][v[1]-1] == 0 and not visited[v[0]][v[1]-1]:
                    que.append([v[0],v[1]-1])
                    visited[v[0]][v[1]-1] = True
                    
            
            result += 1
print(result)
