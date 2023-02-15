from collections import deque
def solution(maps):
    answer = -1
    s = deque([(0,0)])
    n = len(maps)-1
    m = len(maps[0])-1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    maps[0][0] = 100001
    while s:
        x,y = s.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= n and 0 <= ny <= m and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y]+1
                s.append((nx,ny))
    if maps[n][m] == 1:
        return -1
    return maps[n][m]-100000
