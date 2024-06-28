import math
def solution(n, k):
    answer = []
    l = list(range(1,n+1))
    k-=1
    def factorial(t):
        f = 1
        for i in range(1,t+1):
            f*=i
        return f
    for i in range(1,n+1):
        answer.append(l.pop(k//math.factorial(n-i)))
        k = k%math.factorial(n-i)
    
    return answer