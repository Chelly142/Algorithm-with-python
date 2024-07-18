import sys
input = sys.stdin.readline


n, m, k = map(int,input().split())
board = [list(input().rstrip()) for _ in range(n)]

black_start_prefix_count = [[0]*(m+1) for _ in range(n+1)]
white_start_prefix_count = [[0]*(m+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        if (i+j)%2==0:
            if board[i-1][j-1]=="B":
                black_start_prefix_count[i][j] = 0+black_start_prefix_count[i-1][j]+black_start_prefix_count[i][j-1]-black_start_prefix_count[i-1][j-1]
                white_start_prefix_count[i][j] = 1+white_start_prefix_count[i-1][j]+white_start_prefix_count[i][j-1]-white_start_prefix_count[i-1][j-1]
            if board[i-1][j-1]=="W":
                black_start_prefix_count[i][j] = 1+black_start_prefix_count[i-1][j]+black_start_prefix_count[i][j-1]-black_start_prefix_count[i-1][j-1]
                white_start_prefix_count[i][j] = 0+white_start_prefix_count[i-1][j]+white_start_prefix_count[i][j-1]-white_start_prefix_count[i-1][j-1]
        else:
            if board[i-1][j-1]=="W":
                black_start_prefix_count[i][j] = 0+black_start_prefix_count[i-1][j]+black_start_prefix_count[i][j-1]-black_start_prefix_count[i-1][j-1]
                white_start_prefix_count[i][j] = 1+white_start_prefix_count[i-1][j]+white_start_prefix_count[i][j-1]-white_start_prefix_count[i-1][j-1]
            if board[i-1][j-1]=="B":
                black_start_prefix_count[i][j] = 1+black_start_prefix_count[i-1][j]+black_start_prefix_count[i][j-1]-black_start_prefix_count[i-1][j-1]
                white_start_prefix_count[i][j] = 0+white_start_prefix_count[i-1][j]+white_start_prefix_count[i][j-1]-white_start_prefix_count[i-1][j-1]
answer = 10e9
for i in range(k,n+1):
    for j in range(k,m+1):
        b = black_start_prefix_count[i][j]-black_start_prefix_count[i-k][j]-black_start_prefix_count[i][j-k]+black_start_prefix_count[i-k][j-k]
        w = white_start_prefix_count[i][j]-white_start_prefix_count[i-k][j]-white_start_prefix_count[i][j-k]+white_start_prefix_count[i-k][j-k]
        answer = min(answer,b,w)
print(answer)