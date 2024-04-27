def solution(food):
    r = ''
    l = ''
    n = len(food)
    for i in range(1,n):
        k = food[i]//2
        r=r+str(i)*k
        l=str(i)*k+l
    return r+'0'+l