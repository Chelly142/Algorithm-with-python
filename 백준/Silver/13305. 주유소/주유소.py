import sys
input = sys.stdin.readline


n = int(input())
road = list(map(int,input().split()))
road.append(0)
oil = list(map(int,input().split()))
now_city = 0
drive_distance = 0
while now_city<n:
    for next_city in range(now_city+1,n):
        drive_distance+=road[next_city-1]*oil[now_city]
        if oil[next_city]<oil[now_city]:
            break
    if now_city==next_city:
        break
    now_city = next_city
print(drive_distance)