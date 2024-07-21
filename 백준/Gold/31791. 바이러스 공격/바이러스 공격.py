import sys
import heapq
input = sys.stdin.readline

# 13:53

n, m = map(int,input().split())
tg, tb, x, b = map(int,input().split())
city = [list(input().rstrip()) for _ in range(n)]
virus = set()
for i in range(n):
    for j in range(m):
        if city[i][j] == '*': virus.add((i,j))

# 위 오른쪽 아래 왼쪽
dx = (-1,0,1,0)
dy = (0,1,0,-1)

#bfs


def is_range(x,y):
    return True if 0<=x<n and 0<=y<m else False

q = [(0,i[0],i[1]) for i in virus] # 바이러스가 퍼지기 시작한시간 t, 바이러스 좌표 x, y
visited = set()

while q:
    now_t,x,y = heapq.heappop(q)
    if now_t>tg: break
    if city[x][y] =="#":
        city[x][y] = '*'
    for i in range(4):
        next_x = x+dx[i]
        next_y = y+dy[i]
        next_t = now_t+1
        if is_range(next_x,next_y) and next_t<=tg and (next_x,next_y) not in visited:
            if city[next_x][next_y] == '.':
                visited.add((next_x,next_y))
                city[next_x][next_y] = '*'
                heapq.heappush(q, (next_t,next_x,next_y))
            if city[next_x][next_y] == '#':
                visited.add((next_x,next_y))
                heapq.heappush(q, (next_t+tb,next_x,next_y)) ## 빌딩은 바로다음 시간이 아니라 터지는 시각으로 조정
answer =[]
for i in range(n):
    for j in range(m):
        if city[i][j] != '*':
            answer.append((i+1,j+1))
if len(answer)==0: print(-1)
else: 
    for i in answer: print(*i)
# 14:57 시간초과
