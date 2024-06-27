def solution(n):
    answer = 0
    def bin_check(k):
        c=0
        while k!=0:
            if k%2 == 1:
                c+=1
            k=k//2
        return c
    n_c = bin_check(n)
    t = n+1
    while n_c!=bin_check(t):
        t+=1
    return t