def solution(n):
    answer = 0
    for i in range(1,n+1):
        if i%2==0:
            if (n-(i+1)*(i/2))%i==0 and n>=(i+1)*(i/2):
                answer +=1
        if i%2==1:
            if (n-(i//2+1)*i)%i==0 and n>=(i//2+1)*i:
                answer+=1
    return answer
