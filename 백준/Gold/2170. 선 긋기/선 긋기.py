import sys
import heapq
input = sys.stdin.readline

# 12:20
# 3차원 그래프
# 겹치는 구역 찾기 문제
# 모든 점 루프도는 부르트포스는 안되겠고
# n개 돌면서 2개 겹치는 부분 찾고
# 12:32 알고리즘 분류 확인 
# 3차원 누적합? 스위핑? 좌표 압축?
# n, k = map(int, input().split())
# fish_territory = [list(map(int, input().split())) for _ in range(n)]
# fish_territory.sort()
# prefix_sum = []


n = int(input())
lines = [tuple(map(int,input().split())) for _ in range(n)]

lines.sort()
answer = 0
s=lines[0][0]
e=lines[0][1]
for i in range(1,n):
    if e >= lines[i][0]:
        if e>=lines[i][1]:
            continue
        else:
            e = lines[i][1]
    else:
        answer+=(e-s)
        s = lines[i][0]
        e = lines[i][1]
answer+=(e-s)
print(answer)