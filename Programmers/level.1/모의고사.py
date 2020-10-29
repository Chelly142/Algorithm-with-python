def solution(answers):
    n = len(answers)
    l1 = [(i%5+1) for i in range(n)]
    l2 = [2,1,2,3,2,4,2,5]
    l3 = [3,3,1,1,2,2,4,4,5,5]
    l2 = l2*(n//8)+l2[0:n%8]
    l3 = l3*(n//10)+l3[0:n%10]
    
    a,b,c=0,0,0
    for i in range(n):
        if answers[i]==l1[i]:
            a+=1
        if answers[i]==l2[i]:
            b+=1
        if answers[i]==l3[i]:
            c+=1
    k = [a,b,c]
    answer = []
    if max(k) == a:
        answer.append(1)
    if max(k) == b:
        answer.append(2)
    if max(k) == c:
        answer.append(3)
    return answer
