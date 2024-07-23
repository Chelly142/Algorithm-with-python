import sys
input = sys.stdin.readline

#12:40 
n, c = map(int,input().split())
houses = []
for i in range(n):
    houses.append(int(input()))
houses.sort()

def is_possible(mid):
    now_house = houses[0]
    mid_c = 1
    for i in range(n):
        nxt_house = houses[i]
        if nxt_house-now_house>=mid:
            mid_c+=1
            now_house = nxt_house
        if mid_c>=c:
            return True
    for i in range(n-1,-1,-1):
        nxt_house = houses[i]
        if nxt_house-now_house>=mid:
            mid_c+=1
            now_house = nxt_house
        if mid_c>=c:
            return True
    return False

start ,end = 1,max(houses)

while start<=end:
    mid = (start+end)//2

    if is_possible(mid):
        start = mid+1
    else:
        end = mid-1
print(end)