def solution(a, b):
    l = max(a,b)
    s = min(a,b)
    answer = (l*(l+1)-(s)*(s-1))/2
    return answer
