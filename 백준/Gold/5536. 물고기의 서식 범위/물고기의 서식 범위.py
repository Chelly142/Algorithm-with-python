import sys
input = sys.stdin.readline

# 12:20
# 3차원 그래프
# 겹치는 구역 찾기 문제
# 모든 점 루프도는 부르트포스는 안되겠고
# n개 돌면서 2개 겹치는 부분 찾고
# 12:32 알고리즘 분류 확인 
# 3차원 누적합? 스위핑? 좌표 압축?
n, k = map(int, input().split())
fish_territory = []
fish_x = set()
fish_y = set()
fish_d = set()
for i in range(n):
    x1,y1,d1,x2,y2,d2 = map(int, input().split())
    fish_territory.append(((x1,y1,d1),(x2,y2,d2)))
    fish_x.add(x1)
    fish_y.add(y1)
    fish_d.add(d1)
    fish_x.add(x2)
    fish_y.add(y2)
    fish_d.add(d2)
arr_x = sorted(fish_x)
arr_y = sorted(fish_y)
arr_d = sorted(fish_d)

comp_x = {arr_x[i]:i for i in range(len(arr_x))}
comp_y = {arr_y[i]:i for i in range(len(arr_y))}
comp_d = {arr_d[i]:i for i in range(len(arr_d))}

comp_reverse_x = {i:arr_x[i] for i in range(len(arr_x))}
comp_reverse_y = {i:arr_y[i] for i in range(len(arr_y))}
comp_reverse_d = {i:arr_d[i] for i in range(len(arr_d))}


fish_comp_territory = []
for s, e in fish_territory:
    x1,y1,d1 = s
    x2,y2,d2 = e
    fish_comp_territory.append(((comp_x[x1],comp_y[y1],comp_d[d1]), (comp_x[x2],comp_y[y2],comp_d[d2])))

fish_comp_territory.sort()
prefix_sum = [[[0]*(2*n) for _ in range(2*n)] for _ in range(2*n)]
answer = 0
for start, end in fish_comp_territory:
    start_x, start_y, start_d = start
    end_x, end_y, end_d = end
    for x in range(start_x,end_x):
        for y in range(start_y,end_y):
            for d in range(start_d,end_d):
                if prefix_sum[x][y][d] ==-1:
                    continue
                if prefix_sum[x][y][d]<k:
                    prefix_sum[x][y][d]+=1
                if prefix_sum[x][y][d] ==k:
                    answer+=(comp_reverse_x[x+1]-comp_reverse_x[x])*(comp_reverse_y[y+1]-comp_reverse_y[y])*(comp_reverse_d[d+1]-comp_reverse_d[d])
                    prefix_sum[x][y][d] = -1
                
print(answer)
    
    
            