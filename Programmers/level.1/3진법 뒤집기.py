def solution(n):
    answer =0
    l =[]
    while(n>2):
        l.append(n%3)
        n = n//3
    l.append(n)
    t = len(l)
    for i in l:
        t = t-1
        answer = answer + i*(3**t)
    return answer
