def solution(arr):
    answer = max(arr)
    arr.sort(reverse =True)
    
    for i in arr:
        cnt = 1
        while (answer*cnt)%i!=0:
            cnt+=1
        answer = answer*cnt
        
    return answer