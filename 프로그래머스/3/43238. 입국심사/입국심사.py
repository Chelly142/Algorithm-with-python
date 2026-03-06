import bisect

def solution(n, times):
    answer = 0
    def is_possible(time):
        k = 0
        for t in times:
            k+=time//t
        return k>=n
    left = 0
    right = max(times)*n
    while(left<right):
        mid = (left+right)//2
        if is_possible(mid):
            answer = mid
            right = mid
        else:
            left = mid+1
        
    return answer