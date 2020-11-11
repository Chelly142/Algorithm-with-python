def solution(w,h):
    answer = 1
    m = 0
    for i in range(min(w,h),0,-1):
        if w%i==0 and h%i==0:
            m = i
            break
    a = w / m
    b = h / m
    answer = w*h-m*(a+b-1)
    return answer
    #w*h-w-h+m
