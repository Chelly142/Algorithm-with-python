import sys
import copy
input = sys.stdin.readline

board = [list(map(int,input().split())) for _ in range(9)]
zeros=[]
for i in range(9):
    for j in range(9):
        if board[i][j]==0:
            zeros.append((i,j))


def get_pos(x,y):
    impos = set()
    for i in range(9): #가로 세로
        if board[x][i] !=0:
            impos.add(board[x][i])
        if board[i][y] !=0:
            impos.add(board[i][y])
    for i in range(3):
        for j in range(3):
            k = board[(x//3)*3+i][(y//3)*3+j]
            if k!=0:
                impos.add(k)
    return [i for i in range(1,10) if i not in impos]

def print_sudoku(b):
    for i in b:
        print(*i)
def back(z):
    if z==len(zeros):
        print_sudoku(board)
        quit(0)
    else:
        p = zeros[z]
        x,y = p
        pos = get_pos(x,y)
        for next_p in pos:
            board[x][y] = next_p
            back(z+1)
            board[x][y] = 0
back(0)