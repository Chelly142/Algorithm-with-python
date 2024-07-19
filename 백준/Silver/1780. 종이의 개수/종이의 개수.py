import sys
input = sys.stdin.readline

n = int(input())
paper = [list(map(int,input().split())) for _ in range(n)]
paper_cnt = {1:0, 0:0, -1:0}
def is_all_collect(point, side_len):
    x,y = point
    base = paper[x][y]
    for i in range(x,x+side_len):
        for j in range(y,y+side_len):
            if paper[i][j] != base:
                return False
    return True
def dnc(point, side_len):
    x,y = point
    
    if is_all_collect(point, side_len):
        paper_cnt[paper[x][y]]+=1
        return
    
    next_side_len = side_len//3
    for i in range(3):
        for j in range(3):
            dnc((x+i*next_side_len, y+j*next_side_len), next_side_len)

dnc((0,0), n)
print(paper_cnt[-1])
print(paper_cnt[0])
print(paper_cnt[1])
