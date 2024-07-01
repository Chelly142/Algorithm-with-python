def solution(n, s):
    answer = []
    a = s//n
    b = s%n
    answer = [a]*n
    if n>s:
        return [-1]
    for i in range(b):
        answer[-(i+1)]=answer[-(i+1)]+1
    
    return answer