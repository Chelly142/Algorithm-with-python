def solution(board):
    answer = board[0][0]
    nx = len(board)
    ny = len(board[0])
    for i in range(1,nx):
        for j in range(1,ny):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j],board[i][j-1],board[i-1][j-1])+1
            answer = max(board[i][j],answer)
    return answer**2