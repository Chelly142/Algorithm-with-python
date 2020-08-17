def spin_matrix(key):
    n=len(key)
    m=len(key[0])
    new_key =[[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new_key[j][len(key)-i-1] = key[i][j]
    return new_key

def lock_pivot(lock):
    for i,v in enumerate(lock):
        for j,k in enumerate(v):
            if k==0:
                return [i,j]
def key_move(key,d):
    mk=[[0]*len(key) for _ in range(len(key))]
    for i in range(len(key)):
        a=i+d[0]
        if -1<a<len(key):
            for j in range(len(key)):
                b= j+d[1]
                if -1<b<len(key) and key[i][j]:
                    mk[a][b] = key[i][j]
    return mk
                
    
def try_unlock(key,lock):
    for i in range(len(key)):
        for j in range(len(key)):
            if key[i][j]+lock[i][j]!=1:
                return False
    return True
                

def solution(key, lock):
    n = len(lock)
    m = len(key)
    for i in range(m):
        for _ in range(n-m):
            key[i].append(0)
    key+=([[0]*n]*(n-m))
    lp = lock_pivot(lock)
    for c in range(4):
        key = spin_matrix(key)
        for i,v in enumerate(key):
            for j,k in enumerate(v):
                if k==1:
                    kp = [i,j]
                    d = [lp[0]-i,lp[1]-j]
                    if try_unlock(key_move(key, d),lock):
                        return True
                    
    return False
