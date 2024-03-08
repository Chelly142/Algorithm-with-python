def solution(board):
    answer = 0
    n = len(board)
    new_board = [[0]*(n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                new_board[i+1][j+1]=1
    
    for i in range(1,n+1):
        for j in range(1,n+1):
            if new_board[i][j]==1:
                if new_board[i-1][j-1] != 1:
                    new_board[i-1][j-1] = -1
                if new_board[i-1][j] != 1:
                    new_board[i-1][j] = -1
                if new_board[i-1][j+1] != 1:
                    new_board[i-1][j+1] = -1
                if new_board[i][j-1] != 1:
                    new_board[i][j-1] = -1
                if new_board[i][j+1] != 1:
                    new_board[i][j+1] = -1
                if new_board[i+1][j-1] != 1:
                    new_board[i+1][j-1] = -1
                if new_board[i+1][j] != 1:
                    new_board[i+1][j] = -1
                if new_board[i+1][j+1] != 1:
                    new_board[i+1][j+1] = -1
    for i in range(1,n+1):
        for j in range(1,n+1):
            if new_board[i][j]==0:
                answer+=1
            
                    
                    
    return answer