def solution(t, p):
    answer = 0
    p_l = len(p)
    t_l = len(t)
    int_p = int(p)
    for i in range(t_l-p_l+1):
        if int_p >= int(t[i:i+p_l]):
            answer+=1
        
    return answer