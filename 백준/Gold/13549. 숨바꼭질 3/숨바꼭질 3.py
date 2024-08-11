import sys
import heapq
input = sys.stdin.readline

n, k = map(int, input().split())


q=[(0,n)]
check = [int(1e9)] * 100001
check[n] = 0
while q:
    seconds,now_position = heapq.heappop(q)
    if check[k] != int(1e9):
        print(check[k])
        break

    if 0 <= now_position*2 < 100001 and check[now_position*2] == int(1e9):
        check[now_position*2] = seconds
        heapq.heappush(q,(seconds,now_position*2))
    if  0 <= now_position+1 < 100001 and check[now_position+1] == int(1e9):
        check[now_position+1] = seconds+1
        heapq.heappush(q,(seconds+1,now_position+1))

    if  0 <= now_position-1 < 100001 and check[now_position-1] == int(1e9):
        check[now_position-1] = seconds+1
        heapq.heappush(q,(seconds+1,now_position-1))