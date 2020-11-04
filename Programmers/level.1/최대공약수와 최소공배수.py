def solution(n, m):
    answer = [0,0]
    for i in range(min(n,m),0,-1):
        if n%i == 0 and m%i ==0:
            answer[0] = i
            break
    for i in range(max(n,m),max(n,m)*min(n,m)+1):
        if i%n==0 and i%m == 0:
            answer[1] = i
            break
    return answer
