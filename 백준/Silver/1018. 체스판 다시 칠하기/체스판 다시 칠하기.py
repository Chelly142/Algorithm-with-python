import sys
input = sys.stdin.readline

x, y= map(int, input().split())
# c= int(input())
g = [input() for _ in range(x)]
p = ["WBWBWBWB","BWBWBWBW"]
answer =1e9
for i in range(x-7):
    for j in range(y-7):
            m=0
            for k in range(8):
                 for l in range(8):
                    if p[k%2][l]!=g[i+k][j:j+8][l]:
                         m+=1
            answer = min(answer,m, 64-m)
            
print(answer)                
                    

                        