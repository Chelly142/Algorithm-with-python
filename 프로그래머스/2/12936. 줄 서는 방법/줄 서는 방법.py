import math
def solution(n, k):
    answer = []
    l = list(range(1,n+1))
    k-=1
    for i in range(1,n+1):
        fact = math.factorial(n-i)
        answer.append(l.pop(k//fact))
        k = k%fact
    
    return answer