def solution(num, total):
    answer = []
    n = total//num
    if num % 2 ==0:
        for i in range(num):
            answer.append(n-num/2+1+i)
    else:
        for i in range(num):
            answer.append(n-num//2+i)
    return answer