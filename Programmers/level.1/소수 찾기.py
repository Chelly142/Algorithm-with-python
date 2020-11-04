def solution(n):
    answer = 1
    if n == 2: return 1
    prime_num = [2]
    for i in range(3,n+1,2):
        flag = True
        for j in range(3,int(i**0.5)+1):
            if i%j == 0:
                flag = False
                break
        if flag:
            answer = answer+1       
    return answer
