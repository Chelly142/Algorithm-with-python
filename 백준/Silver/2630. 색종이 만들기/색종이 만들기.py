import sys
input = sys.stdin.readline

n = int(input())

paper = [list(map(int,input().split())) for _ in range(n)]
b_cnt, w_cnt = 0,0
def is_complete(n,paper):
    return sum([sum(i) for i in paper]) in [0,n**2]

def dnc(n, paper):
    global b_cnt
    global w_cnt
    if is_complete(n,paper):
        if paper[0][0]==1:
            b_cnt+=1
        else:
            w_cnt+=1
        return
    else:
        cut_paper_1 = [[0]*(n//2) for _ in range(n//2)]
        cut_paper_2 = [[0]*(n//2) for _ in range(n//2)]
        cut_paper_3 = [[0]*(n//2) for _ in range(n//2)]
        cut_paper_4 = [[0]*(n//2) for _ in range(n//2)]
        for i in range(n):
            for j in range(n):
                if i<n//2 and j<n//2:
                   cut_paper_1[i][j] = paper[i][j]
                if i<n//2 and n//2<=j:
                    cut_paper_2[i][j-n//2] = paper[i][j]
                if n//2<=i and j<n//2:
                    cut_paper_3[i-n//2][j] = paper[i][j]
                if n//2<=i and n//2<=j:
                    cut_paper_4[i-n//2][j-n//2] = paper[i][j]

        dnc(n//2,cut_paper_1)
        dnc(n//2,cut_paper_2)
        dnc(n//2,cut_paper_3)
        dnc(n//2,cut_paper_4)

dnc(n,paper)
print(w_cnt)
print(b_cnt)