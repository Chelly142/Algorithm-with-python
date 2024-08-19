from itertools import combinations
import sys
input = sys.stdin.readline

n, c = map(int, input().split())
knapsacks = list(map(int, input().split()))
knapsacks.sort()

left_arr = knapsacks[:n//2]
right_arr = knapsacks[n//2:]

answer = 0

def search(arr):
    global answer
    s_arr = [0]
    for i in range(1,len(arr)+1):
        for combi in combinations(arr,i):            
            s =sum(combi)
            s_arr.append(s)
    return s_arr

left_sum_arr = search(left_arr)
left_sum_arr.sort()
right_sum_arr = search(right_arr)
right_sum_arr.sort()


for element_left in left_sum_arr:
    left = 0
    right = len(right_sum_arr)-1
    while left<=right:
        mid = (left+right)//2
        if right_sum_arr[mid]+element_left<=c:
            left = mid+1
        else:
            right= mid-1
    answer+=(right+1)
print(answer)