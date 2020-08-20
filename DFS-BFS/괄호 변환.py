def correct(s):
    count = 0
    for i in s:
        if i=="(":
            count+=1
        else:
            if count==0:
                return False
            count-=1
    return True
    
def solution(p):
    if p=="":
        return ""
    c_c = 0
    c_o = 0
    for i in p:
        if i =="(":
            c_o+=1
        else:
            c_c+=1
        if c_o==c_c:
            u = p[:c_c+c_o]
            v = p[c_c+c_o:]
            break
    if correct(u):
        return u+solution(v)
    else:
        t = "("+solution(v)+")"
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i]=="(":
                u[i]=')'
            else:
                u[i]='('
        return t+"".join(u)
    return False
